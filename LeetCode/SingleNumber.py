# https://leetcode.com/problems/single-number/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      # sort input list
      nums.sort()
      # define aux variable as index and initialize it with 0
      index = 0
      # iteract through list until length -1
      while index < len(nums)-1:
        # test two consecutive numbers (list is sorted)
        if nums[index] != nums[index+1]:
          # different then the number is in the index position
          return nums[index]
        # update index by 2
        index +=2
      
      # test last postiion
      if index == len(nums)-1:
        return nums[index]

      # no possible solution
      return -1

s = Solution()

lst = [2,2,1]   
print(s.singleNumber(lst)) 

lst = [4,1,2,1,2]   
print(s.singleNumber(lst)) 

lst = []   
print(s.singleNumber(lst)) 

lst = [1,2,1,2]   
print(s.singleNumber(lst)) 