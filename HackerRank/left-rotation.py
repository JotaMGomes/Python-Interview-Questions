# https://www.hackerrank.com/challenges/array-left-rotation/problem
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
    nums[:] = nums[k:] + nums[:k]


if __name__ == '__main__':
  s = Solution()

  vNums01 = [1,2,3,4,5]
  vTarget01 = 4
  s.rotate(vNums01, vTarget01)
  print(vNums01)