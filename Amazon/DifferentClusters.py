# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def am(self, r: int, c:int, vl:List)->int:

    def findCluster(x:int, y:int):
      vl[x][y] = -1
      if y < c -1:
        if vl[x][y+1] == 1:
          findCluster(x, y+1)
      if y > 0:
        if vl[x][y-1] == 1:
          findCluster(x, y-1)
      if x < r -1:
        if vl[x+1][y] == 1:
          findCluster(x+1, y)
      if x > 0:
        if vl[x-1][y] == 1:
          findCluster(x-1, y)   
      return                       

    numC = 0
    for i in range(r):
      for j in range(c):
        if vl[i][j] == 1:
          numC +=1
          findCluster(i, j)
    
    return numC



if __name__ == '__main__':
  s = Solution()
  print(s.am(5,4,[[1,1,0,0],
                  [0,0,1,0],
                  [0,0,0,0],
                  [1,0,1,1],
                  [1,1,1,1]]))

  print(s.am(5,4,[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]))

  print(s.am(5,4,[[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]])) 

  print(s.am(5,4,[[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,1,0],
                  [0,0,0,1]]))                                     