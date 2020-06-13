# https://leetcode.com/problems/reverse-integer/
# Jose Luiz Mattos Gomes

class Solution:
  def reverse(self, x: int) -> int:
    # define auxiliar variable to help with calculations
    y = abs(x)
    # define vReturn variable
    vReturn = 0
    
    # keep calculation while y > 0
    while y > 0:
      vReturn = vReturn*10 + y%10
      y= y//10
    
    # if returning number is higher then 2^31 then return 0
    if vReturn > 2**31:
      return 0

    # deal with sign
    if x < 0:
      return -1*vReturn
    else:
      return vReturn


s = Solution()

print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(21))
print(s.reverse(1563847412))
print(s.reverse(1534236469))