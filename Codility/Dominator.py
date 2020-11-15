# https://app.codility.com/programmers/lessons/8-leader/dominator/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, A:List)->int:
    if len(A) == 0:
      return -1
    l = {}
    max = 0
    i = 0
    d = -1
    while i < len(A):
      a = A[i]
      if a in l:
        l[a].append(i)
      else:
        l[a]=[i]
     
      if len(l[a]) > max:
        max = len(l[a])
        d = a      
      
      i+=1
    
    if max <= len(A) / 2:
      return -1
   
    return l[d][0]



if __name__ == "__main__":
  s = Solution()
  print(s.s([3,4,3,2,3,-1,3,3]))
  print(s.s([2147483647]))
  print(s.s([2, 1, 1, 3]))