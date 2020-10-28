# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def am1(self, vl:List, d:int)->List:
    i = 1
    v1 = vl.copy()
    while i <= d:
      ant = 0
      pos = 0
      j = 0
      while j < len(vl):
        if j > 0:
          ant = vl[j-1]
        if j < len(vl) -1:
          pos = vl[j+1]
        else:
          pos = 0

        if ant == pos:
          v1[j] = 0
        else:
          v1[j] = 1
        j +=1
      
      vl = v1.copy()
      i +=1
    
    return v1
          
  def cellCompete(self, states, days):
      n = len(states)
      for day in range(days):
          houses = [0] + states + [0]
          states = [houses[i-1] ^ houses[i+1] for i in range(1, n+1)] # ^ = XOR
      return states    

if __name__ == '__main__':
  s = Solution()
  print(s.am1([1,0,0,0,0,1,0,0], 1))
  print(s.am1([1,1,1,0,1,1,1,1], 2))
  print("====")
  print(s.cellCompete([1,0,0,0,0,1,0,0], 1))
  print(s.cellCompete([1,1,1,0,1,1,1,1], 2))