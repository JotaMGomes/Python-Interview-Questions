# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, A:List)->int:
    A.sort()
    i = 0
    while i < len(A)-1:
      if A[i] != A[i+1]:
        return A[i]
      i+=2
    
    return A[-1]


if __name__ == '__main__':
  s = Solution()
  print(s.s([9,3,9,3,9,7,9]))
  print(s.s([1,1,2,2,3]))

