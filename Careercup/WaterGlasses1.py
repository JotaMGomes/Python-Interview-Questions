# https://www.careercup.com/question?id=22191662
# Jose Luiz Mattos Gomes

class TreeNode:
  def __init__ (self, n:int, l = None, r = None):
    self.n = n
    self.l = r
    self.r = l 


class Solution:
  def s(self):
    pass


if __name__ == "__main__":

  wg = TreeNode(0)     # 1 
  aux = TreeNode(0)    # 2 
  wg.l = aux           # 1 > 2, None
  aux = TreeNode(0)    # 3 
  wg.r = aux           # 1 > 2, 3
  
  aux = wg.l           # 2
  aux1 = TreeNode(0)   # 4
  aux.l = aux1         # 2 > 4, None
  aux1 = TreeNode(0)   # 5
  aux.r = aux1         # 2 > 4, 5

  aux = wg.r           # 3
  aux.l = aux1         # 3 > 5, None
  aux1 = TreeNode(0)   # 6
  aux.r = aux1         # 3 > 5, 6

  aux = wg.l           # 2
  aux = aux.l          # 4
  aux1 = TreeNode(0)   # 7
  aux.l = aux1         # 4 > 7, None
  aux1 = TreeNode(0)   # 8
  aux.r = aux1         # 4 > 7, 8

  aux = wg.l           # 2
  aux = aux.r          # 5
  aux.l = aux1         # 5 > 8, None
  aux1 = TreeNode(0)   # 9
  aux.r = aux1         # 5 > 8, 9

  aux = wg.r           # 3
  aux = aux.r          # 6
  aux.l = aux1         # 6 > 9, None
  aux1 = TreeNode(0)   # 10
  aux.r = aux1         # 6 > 9, 10

  s = Solution()
  s.s()