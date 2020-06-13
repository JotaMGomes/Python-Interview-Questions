# https://leetcode.com/problems/valid-parentheses/
# Jose Luiz Mattos Gomes

class Solution:
  def isValid(self, s: str) -> bool:
    # define empty list that will work as a "stack"
    vList = []
    # iteract througn s
    for i in s:
      if i == ')':
        # test if vList is empty and if last char as a '('
        if len(vList)==0 or vList.pop() != '(':
          # stack is empty or type of brackets do not match 
          return False
      elif i == ']':
        # test if vList is empty and if last char as a '['
        if len(vList)==0 or vList.pop() != '[':
          # stack is empty or type of brackets do not match 
          return False
      elif i == '}':
        # test if vList is empty and if last char as a '{'
        if len(vList)==0 or vList.pop() != '{':
          # stack is empty or type of brackets do not match 
          return False
      else:
        # add open symbol
        vList.append(i)

    # in order to return true, list must be empty
    return len(vList)==0


s = Solution()

print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("}"))