# https://app.codility.com/programmers/lessons/6-sorting/triangle/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:

  def s(sel, A:List)->int:
    A.sort()
    i = 0
    if len(A) < 3:
      return 0
   
    while i < len(A)-2:
      # A is sorted so:
      # A[i+2] > A[i]   -> A[i+2] + A[i+1] > A[i]
      # A[i+2] > A[i+1] -> A[i+2] + A[i]   > A[i+1]
      # A[i+3] > A[i+2], so only need to test A[i] + A[i+1] > A[i+2]
      if A[i] + A[i+1] > A[i+2]:
            #print(A[i], A[i+1], A[i+2])
            return 1
      i+=1
    return 0    



if __name__ == "__main__":
  s = Solution()
  print(s.s([10,2,5,1,8,20]))  
  print(s.s([10,50,5,1])) 