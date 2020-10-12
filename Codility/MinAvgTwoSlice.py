# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
# Jose Luiz Mattos Gomes

import sys

class Solution:
  def solution(self, A):
    i = 0
    pos = -1
    minAvg = sys.maxsize
    while i < len(A) - 1:
      x = sum(A[i:i+2])/2
      if x < minAvg:
        minAvg = x
        pos = i
      i +=1

    if len(A) > 2:
      i = 0
      while i < len(A) - 2:
        x = sum(A[i:i+3])/3
        if x < minAvg:
          minAvg = x
          pos = i
        i +=1
    return pos          


if __name__ == '__main__':
  s = Solution()
  print(s.solution([4,2,2,5,1,5,8]))
  print(s.solution([-3, -5, -8, -4, -10]))
  print(s.solution([1, 7, 7, 1]))
