# https://www.careercup.com/question?id=22191662
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, vl: List, l:int):
    i = 0
    while i < len(vl) and l > 0:
      j = 0
      while j < len(vl[i]) and l > 0:
        if i == 0 and j == 0:
          vl[i][j] = l
          l -=1

        if vl[i][j] > 1:
          if i < len(vl) -1:
            vl[i+1][j] = vl[i+1][j] + ((vl[i][j] - 1) / 2)
            vl[i+1][j+1] = vl[i+1][j+1] + ((vl[i][j] - 1) / 2)
            vl[i][j] = 1
            l -= 1
        
        j += 1
      i +=1
    
    s = 0
    i = 0
    while i < len(vl):
      j = 0
      while j < len(vl[i]):
        s +=1
        if vl[i][j] > 0:
          print(str(s) + ': ' + str(vl[i][j]))
        j +=1
      i+=1




if __name__ == "__main__":

  s = Solution()
  s.s([[0],[0,0],[0,0,0],[0,0,0,0]], 2)
  print("====")
  s.s([[0],[0,0],[0,0,0],[0,0,0,0]], 5)
  print("====")
  s.s([[0],[0,0],[0,0,0],[0,0,0,0]], 6)