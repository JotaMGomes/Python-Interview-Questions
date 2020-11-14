# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(sel, S)->int:
    q = []
    for c in S:
      if c in ['{','[','(']:
        q.append(c)
      else:
        if len(q) == 0:
          return 0
        elif c == ')':
          if q.pop() != '(':
            return 0
        elif c == ']':
          if q.pop() != '[':
            return 0
        else:
          if q.pop() != '{':
            return 0
    
    if len(q) == 0:
      return 1
    else:
      return 0



if __name__ == "__main__":
  s = Solution()
  print(s.s("{[()()]}"))
  print(s.s("([)()]"))
