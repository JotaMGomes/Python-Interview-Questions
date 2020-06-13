# https://leetcode.com/problems/valid-palindrome/
# Jose Luiz Mattos Gomes

class Solution:
  def isPalindrome(self, s: str) -> bool:
    # test var size
    if len(s) < 2:
      return True
    # define left and right pointers
    left=0
    right=len(s)-1
    # loop while left < right
    while left < right:
      # test for alphanumeric chars
      if not s[left].isalnum():
        left +=1
        continue

      if not s[right].isalnum():
        right -=1
        continue

      # test is chars at left and right posision are equal, ignore case
      if not s[left].upper() == s[right].upper():
        return False
      
      # update pointers
      left +=1
      right -=1
    
    # str is a palindrome
    return True






s = Solution()

print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome("0P0"))
print(s.isPalindrome("0P"))