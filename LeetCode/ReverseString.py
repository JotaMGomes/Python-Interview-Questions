# https://leetcode.com/problems/sort-colors/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def reverseString(self, s: List[str]) -> None:
    # iteract througn half the list
    for index in range(int(len(s)/2)):
      # store char in a temp variable
      vChar = s[index]
      # change current char to the char on the oposite index of the list
      s[index] = s[len(s)-(index+1)]
      # change the char in the oposite index to the char in the temp variable
      s[len(s)-(index+1)] = vChar


s = Solution()

s01 = ['h','e','l','l','o']
s.reverseString(s01)
print(s01)

s01 = ['H','a','n','n','a','h']
s.reverseString(s01)
print(s01)