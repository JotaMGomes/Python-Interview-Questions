# https://leetcode.com/problems/sort-colors/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # define the result list
    vResult = [-1,-1]
    # define list to store tested values
    hmNums = []
    # auxiliar variable to keep index
    index=0
    
    # iteract through input list
    for i in nums:
      # store remainder value
      remainder = target - i
      # test if remainder value is already on my tested list
      if remainder in hmNums:
        # store indexes found
        vResult[0]=index
        vResult[1]=hmNums.index(remainder)
        # return found values
        return vResult

      # increment index value
      index +=1
      # store tested value
      hmNums.append(i)
    # no value found 
    return vResult


s = Solution()

vNums01 = [2, 7, 11, 15]
vTarget01 = 9
print(s.twoSum(vNums01, vTarget01))

vNums01 = [2, 7, 11, 15]
vTarget01 = 26
print(s.twoSum(vNums01, vTarget01))

vNums01 = []
vTarget01 = 0
print(s.twoSum(vNums01, vTarget01))