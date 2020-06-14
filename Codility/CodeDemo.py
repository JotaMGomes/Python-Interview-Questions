# https://app.codility.com/demo/take-sample-test/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def solution(self, A: List) -> int:
    # sort input list
    A.sort()
    # test if '1' is in the list
    if not 1 in A:
      return 1

    # find the index of '1' e add 1
    index = A.index(1)+1
    # define return variable
    minNum = 1

    # iteract from index to len(A)
    while index < len(A):
      # test if current number is previous +1
      if A[index] != minNum+1:
        # test if current number is equal to previous
        if A[index] != minNum:
          # the number that does not occur in A = minNum+1
          return minNum+1
        else:
          # update minNum as current number is equal to previous
          minNum -=1

      # update index and minNum
      index +=1
      minNum +=1

    # return last number +1
    return minNum+1


s = Solution()

vNums01 = [1, 3, 6, 4, 1, 2]
print(s.solution(vNums01))
vNums01 = [1, 2, 3]
print(s.solution(vNums01))
vNums01 = [-1, -3]
print(s.solution(vNums01))