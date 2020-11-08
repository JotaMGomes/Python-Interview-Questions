# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
# Jose Luiz Mattos Gomes

class Solution:
  def s(self, S, P, Q):
    r = []
    i = 0
    one = []

    while i < len(P):
      minP, maxP = P[i], Q[i]
      found = False
      for j in one:
        if P[j] >= minP and Q[j] <= maxP:
          one.append(i)
          r.append(1)
          found = True
          break
        
      if found:
        i +=1
        continue
      
      k = S[P[i]:Q[i]+1]
      if 'A' in k:
        r.append(1)
      elif 'C' in k:
        r.append(2)
      elif 'G' in k:
        r.append(3)
      else:
        r.append(4)        

      i +=1
    
    return r

  def s2(self, S, P, Q):
    r = [0] * len(P)
    i = 0
    
    def maxQIndex(p1, p2):
      j = 0
      vq = -1
      vj = -1
      while j < i:
        if P[j] >= p1 and Q[j] <= p2 and r[j] == 1:
            return -2
        if P[j] == p1:
          if Q[j] <= p2:
            if Q[j] > vq:
              vq = Q[j]
              vj = j
        j +=1
      return vj

    def minQIndex(p1, p2):
      j = 0
      vq = Q[i]
      vj = -1
      while j < i:
        if P[j] > p1 and Q[j] <= p2:
          if P[j] < vq:
            vq = P[j]
            vj = j
        j +=1
      return vj      

    i = 0
    while i < len(P):
      vr = 4
      p1, p2 = P[i], Q[i]
      
      while p1 <= p2:
        vi = maxQIndex(p1, p2)
        if vi == -2:
          vr = 1
          break
        elif vi > -1:
          vr = min(vr, r[vi])
          p1 = P[vi]+1
          continue
        
        vj = minQIndex(p1, p2)
        if vj > -1:
          p2 = P[vj]-1

        k = S[p1:p2+1]
        if 'A' in k:
          vr = 1
          break
        elif 'C' in k:
          vr = 2
        elif 'G' in k:
          vr = min(vr, 3)
        else:
          vr = min(vr, 4) 

        p1 = p2+1
        p2 = Q[i]
      
      r[i] = vr
      i +=1

    return r


  def s3(self, S, P, Q):
    r = []
    i = 0
    while i < len(P):
      k = S[P[i]:Q[i]+1]
      if 'A' in k:
        r.append(1)
      elif 'C' in k:
        r.append(2)
      elif 'G' in k:
        r.append(3)
      else:
        r.append(4)

      i +=1
    
    return r    


if __name__ == "__main__":
    s = Solution()
    print(s.s('CAGCCTA', [2,5,0], [4,5,6]))
    print(s.s('AC', [0,0,1], [0,1,1]))
    print(s.s('GT', [0, 0, 1], [0, 1, 1]))

    print(s.s2('CAGCCTA', [2,5,0], [4,5,6]))
    print(s.s2('AC', [0,0,1], [0,1,1]))
    print(s.s2('GT', [0, 0, 1], [0, 1, 1]))

    print(s.s2('CAGCCTA', [2,5,0], [4,5,6]))
    print(s.s2('AC', [0,0,1], [0,1,1]))
    print(s.s2('GT', [0, 0, 1], [0, 1, 1]))
    