# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # define minPrice as max int possible
    minPrice = 2**31
		# define vProfit as min possible 0
    vProfit = 0
		# iteract through prices
    for i in prices:
			# test if current element is smaller than minPrice
      if i < minPrice:
				# update minPrice
        minPrice = i
			# test if profit is higher than vProfit
      elif i - minPrice > vProfit:
				# update vProfit
        vProfit = i - minPrice
		
		
		# return vProfit as maxProfit found
    return vProfit


s = Solution()

vNums01 = [7,1,5,3,6,4]
print(s.maxProfit(vNums01))

vNums01 = []
print(s.maxProfit(vNums01))

vNums01 = [3,2,6,1,3]
print(s.maxProfit(vNums01))

vNums01 = [7,6,4,3,1]
print(s.maxProfit(vNums01))