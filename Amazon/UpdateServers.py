# Jose Luiz Mattos Gomes

from typing import List
import datetime

class Solution:
  def am(self, r: int, c:int, vl:List)->int:
    #print(vl)
    minDays = 0
    hasUpdate = True
    while hasUpdate:
      hasUpdate = False
      foundZero = False
      for i in range(r):
        for j in range(c):
          if vl[i][j] == 0:
            aux = -2^31
            foundZero = True
            
            if i > 0:
              if vl[i-1][j] > 0:
                aux = -1
              elif vl[i-1][j] < 0:
                aux = vl[i-1][j] -1
            
            if i < r -1:
              if vl[i+1][j] > 0:
                aux = max(aux,-1)
              elif vl[i+1][j] < 0:
                aux = max(aux,vl[i+1][j] -1)
            
            if j > 0:
              if vl[i][j-1] > 0:
                aux = max(aux,-1)
              elif vl[i][j-1] < 0:
                aux = max(aux,vl[i][j-1] -1)
            
            
            if j < c -1:
              if vl[i][j+1] > 0:
                aux = max(aux,-1)
              elif vl[i][j+1] < 0:
                aux = max(aux,vl[i][j+1] -1)
          
            if aux > -2^31:
              hasUpdate = True
              vl[i][j] = aux

            if vl[i][j] < minDays:
              minDays = vl[i][j]
      #print(vl)
      #print(minDays)

    if foundZero:
      minDays = 1

    return minDays * -1



  def am2(self, r: int, c:int, vl:List)->int:
    lZeros = []
    numDays = 0
    # print(vl)
    for i in range(r):
      for j in range(c):
        if vl[i][j] == 0:
          lZeros.append([i,j,0])

    flag = len(lZeros) > 0
    while flag:
      flag = False
      for k in lZeros:
        i, j = k[0], k[1]
        
        if i > 0:
          if vl[i-1][j] == 1:
            k[2] = 1
            flag = True
            continue
        
        if i < r -1:
          if vl[i+1][j] == 1:
            k[2] = 1
            flag = True
            continue
        
        if j > 0:
          if vl[i][j-1] > 0:
            k[2] = 1
            flag = True
            continue
        
        if j < c -1:
          if vl[i][j+1] > 0:
            k[2] = 1
            flag = True
            continue      
    
      # print(lZeros)
      k = 0
      while k < len(lZeros):
        # print(lZeros[k])
        m = lZeros[k]
        if m[2] == 1:
          i, j = m[0], m[1]
          vl[i][j] = 1
          lZeros.remove(m)
        else:
          k+=1
      
      # print(vl)
      if flag:
        numDays +=1

    if len(lZeros) > 0:
      return -1
    else:
      return numDays



if __name__ == '__main__':
  s = Solution()
  print(s.am(4,5,[[0,1,1,0,1],
                  [0,1,0,1,0],
                  [0,0,0,0,1],
                  [0,1,0,0,0]]))

  print(s.am(4,5,[[1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1]]))

  print(s.am(4,5,[[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]))

  print(s.am(4,5,[[1,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]))   

  print("=========")

  print(s.am2(4,5,[[0,1,1,0,1],
             [0,1,0,1,0],
             [0,0,0,0,1],
             [0,1,0,0,0]]))
             
  print(s.am2(4,5,[[1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1]]))

  print(s.am2(4,5,[[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]))

  print(s.am2(4,5,[[1,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]))



