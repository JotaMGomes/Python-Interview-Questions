# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def solution(self, A: int) -> int:
    vBinVal = format(A, "b")
    # variable to store max sequence
    maxSeq = 0
    # define counter
    vCounter = 0
    	
    # iteract through vBinVal chars
    for i in range(len(vBinVal)):
      if vBinVal[i]=='1':
        # found a '1'
        if vCounter > maxSeq:
          # update maxSeq if counter is higher than maxSql
          maxSeq = vCounter
        # reset counter
        vCounter = 0
      else:
        # found a '0', update counter
        vCounter +=1
    	
    # return max sequence found
    return maxSeq


s = Solution()

vNum = 9
print(str(vNum) + " " + format(vNum, "b") + " " + str(s.solution(vNum)))
vNum = 561892
print(str(vNum) + " " + format(vNum, "b") + " " + str(s.solution(vNum)))