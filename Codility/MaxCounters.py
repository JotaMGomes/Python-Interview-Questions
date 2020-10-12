# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
# Jose Luiz Mattos Gomes

class Solution:
  def solution(self, N, A):
    # keep max value
    max = 0
    # keep last max value when updated all list
    base = 0
    # create list
    r = [base] * N
    # interact through input list
    for i in A: 
      # if value is higher than N, update base value
      if i > N:
        base = max
      else:
        # if current counter value is higher than base value, just increment
        if r[i-1] >= base:
          r[i-1]+=1
        else:
          # old value, than put base value + 1
          r[i-1] = base + 1
        
        # updat max value if necessary
        if r[i-1] > max:
          max = r[i-1]

    # if any counter is less than the base value, than update to base value
    i = 0
    while i < len(r):
      if r[i] < base:
        r[i] = base
      i +=1

    return r    



if __name__ == '__main__':
  s = Solution()
  print(s.solution(5,[3,4,4,6,1,4,4]))

