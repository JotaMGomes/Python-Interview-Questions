# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, A:List)-> int:
    if len(A) == 0:
      return 1

    A.sort()
    i = 0
    if A[0] != 1:
      return 1

    while i < len(A)-1:
      if A[i]+1 != A[i+1]:
        return A[i] + 1
      i +=1

    return A[-1]+1


if __name__ == '__main__':
  s = Solution()
  print(s.s([2,3,1,5]))
  print(s.s([]))
  print(s.s([2]))
  print(s.s([1]))
  print(s.s([1,2,3,4]))


