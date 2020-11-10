# https://www.tutorialspoint.com/get-unique-values-from-a-list-in-python
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, A:list)->int:
    # use a set to find unique values
    vSet = set(A)
    return len(vSet)

if __name__ == "__main__":
  s = Solution()
  print(s.s([2,1,1,2,3,1]))  