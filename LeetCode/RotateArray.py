# https://leetcode.com/problems/rotate-array/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    # guarantee that k is between 0 and nums.length
    k = k % len(nums)
    # if k is zero than no rotation is needed
    if(k==0):
    	return
    
    # change items
    nums[:] = nums[len(nums)-k:] + nums[: len(nums)-k]



s = Solution()

vNums01 = [1,2,3,4,5,6,7]
vTarget01 = 3
s.rotate(vNums01, vTarget01)
print(vNums01)
s.rotate(vNums01, vTarget01)
vNums01 = [1,2,3,4]
vTarget01 = 4
print(vNums01)