# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, A:List)->int:
    # last position
    i = len(A) - 1
    accOne = 0     # count number of '1'
    passCar = 0    # count number of passing cars
    # loop trough A
    while i >= 0:
      if A[i] == 1:
        accOne +=1
      else:
        # update passCar each time '0' is found
        passCar += accOne
        if passCar > 1000000000:
          return -1
      i -=1
    return passCar



if __name__ == "__main__":
  s = Solution()
  print(s.s([0,1,0,1,1]))