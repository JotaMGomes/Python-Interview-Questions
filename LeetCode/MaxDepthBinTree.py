# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Jose Luiz Mattos Gomes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # define recursive method
    def maxDepth(self, root: TreeNode) -> int:
      if root == None:
        # if is a leaf, return 0
        return 0
      
      # return 1 + next iteration -> (max left, right)
      return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
      

s = Solution()

#    3
#   / \
#  9  20
#    /  \
#   15   7

bt1 = TreeNode(3)
bt1.left = TreeNode(9)
bt1.right = TreeNode(20)

aux = bt1.right
aux.left = TreeNode(15)
aux.right = TreeNode(7)

print(s.maxDepth(bt1))

# -----

#	     3
#	    / \
#	   9  20
#	     /  \
#	    15   7	
#     /  \	
#    12  16
#      \
#     	13	
  
bt2 = TreeNode(3)
bt2.left = TreeNode(9)
bt2.right = TreeNode(20)

aux = bt2.right
aux.left = TreeNode(15)
aux.right = TreeNode(7)

aux = aux.left
aux.left = TreeNode(12)
aux.right = TreeNode(16)

aux = aux.left
aux.right = TreeNode(13)

print(s.maxDepth(bt2))