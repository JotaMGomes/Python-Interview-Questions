# https://app.codility.com/programmers/lessons/8-leader/equi_leader/
# Jose Luiz Mattos Gomes

from typing import List, Dict

class Solution:
  def s(self, A:List)->int:

    def addDict(v:int, d:Dict):
      if v in d:
        d[v] +=1
      else:
        d[v] = 1

    def subDict(v:int, d:Dict):
      d[v] -=1
      if d[v] == 0:
        del d[v]

    def findMax(d:Dict):
      return max(d.values())

    def findKey(v:int, d:Dict)->int:
      for key, value in d.items():
        if value == v:
          return key

    if len(A) < 2:
      return 0

    s1, s2 = {}, {}
    el = 0
    addDict(A[0], s1)
    t1 = 1

    i = 1
    while i < len(A):
      addDict(A[i], s2)
      i +=1
    t2 = len(A)-1      

    #print(s1, findMax(s1))    
    #print(s2, findMax(s2))
    
    l1 = findMax(s1)
    if l1 > t1 / 2:
      l2 = findMax(s2)
      if l2 > t2 / 2:
        if findKey(l1,s1) == findKey(l2, s2):
          el +=1

    i = 1
    while i < len(A)-1:
      addDict(A[i], s1)
      t1 += 1
      subDict(A[i], s2)
      t2 -= 1

      #print(s1, findMax(s1))    
      #print(s2, findMax(s2))

      l1 = findMax(s1)
      if l1 > t1 / 2:
        l2 = findMax(s2)
        if l2 > t2 / 2:
          if findKey(l1,s1) == findKey(l2, s2):
            el +=1

      i +=1

    
    return el




if __name__ == "__main__":
  s = Solution()
  print(s.s([4,3,4,4,4,2]))