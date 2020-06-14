# https://leetcode.com/problems/arranging-coins/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def arrangeCoins(self, n: int) -> int:
    # zero or negative numbers, return 0
    if(n<1):
      return 0
		
    # define accumulator with 0
    acc = 0
    # define counter with 0
    counter = 0
		
    # loop while accumulator <= n
    while acc <= n:
      # increment counter
      counter +=1
      # update accumulator
      acc +=counter
    

    # return counter minus 1
    return counter-1



s = Solution()

print(s.arrangeCoins(5))
print("==========")
print(s.arrangeCoins(8))
print("==========")
print(s.arrangeCoins(0))
print("==========")
print(s.arrangeCoins(2147483647))
print("==========")
print(s.arrangeCoins(6))
