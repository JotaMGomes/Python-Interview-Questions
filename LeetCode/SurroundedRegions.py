# https://leetcode.com/problems/surrounded-regions/
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
      """
      Do not return anything, modify board in-place instead.
      """

      # total lines
      l = len(board)
      if l < 1:
        return

      # total columns
      c = len(board[0])

      # iteract through columns
      for i in range(c):
        # test first line
        if board[0][i] == 'O':
          self.findPath(board, 0, i)
        # test last line
        if board[l-1][i] == 'O':
          self.findPath(board, l-1, i)

      # iteract through lines
      for j in range(l):
        # test first column
        if board[j][0] == 'O':
          self.findPath(board, j, 0)
        # test last column
        if board[j][c-1] == 'O':
          self.findPath(board, j, c-1)  

      # change remaining 'O' to 'X' and 'I' to 'O'
      for i in range(c):  
        for j in range(l):
          if board[j][i] == 'O':
            board[j][i] = 'X'
          if board[j][i] == 'I':
            board[j][i] = 'O'

    # recursive function to change 'O' to 'I' to paths that are not surrounded by 'X'
    def findPath(self, board: List[List[str]], l: int, c: int) -> None:
      # change to a 'I'
      board[l][c] = 'I'
      if c > 0:
        if board[l][c-1] == 'O':
          # test position on the left
          self.findPath(board, l, c-1)
      if c < len(board[0])-1:
        if board[l][c+1] == 'O':
          # test position on the right
          self.findPath(board, l, c+1)
      if l > 0:
        if board[l-1][c] == 'O':
          # test position on the top
          self.findPath(board, l-1, c)
      if l < len(board)-1:
        if board[l+1][c] == 'O':
          # test position on the botton
          self.findPath(board, l+1, c)

s = Solution()

lst = []   
s.solve(lst)
print(lst)

lst = [['O'],
       ['O']]   
s.solve(lst)
print(lst)

lst = ['O']   
s.solve(lst)
print(lst)

lst = [['X','X','X','X'],
       ['X','O','O','X'],
       ['X','X','O','X'],
       ['X','O','X','X']]   
s.solve(lst)
print(lst)

lst = [['X','X','X','X'],
       ['X','O','O','X'],
       ['X','O','O','X'],
       ['X','O','X','X']]   
s.solve(lst)
print(lst)