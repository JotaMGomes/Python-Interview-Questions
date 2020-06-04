# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    # pointers to last index of 0, 1 and 2
    p0, p1, p2 = -1, -1, -1

    # loop through list
    for i in range(len(nums)):
      if nums[i]==0 :
        # found a 0

        # update pointer 2
        if p2>-1 and nums[p2]==2:
          nums[i] = 2
        p2+=1

        # update pointer 1
        if p1 > -1 and nums[p1]==1:
          p1+=1
          nums[p1] = 1
        else:
          p1+=1
        
        # update pointer 0        
        p0+=1
        nums[p0] = 0
      
      elif nums[i] ==1:
        # found a 1
        
        # update pointer 2
        if p2>-1 and nums[p2]==2:
          nums[i] = 2
        p2+=1

        #update pointer 1
        p1+=1
        nums[p1] = 1        
      else:
        # found a 2

        # update pointer 2
        p2+=1
      # print(nums)


s = Solution()

arrayInt = [2,0,2,1,1,0]
print(arrayInt)
s.sortColors(arrayInt)
print(arrayInt)

arrayInt = [0,2,1]
print(arrayInt)
s.sortColors(arrayInt)
print(arrayInt)