# https://www.hackerrank.com/challenges/2d-array/problem
# Jose Luiz Mattos Gomes

class Solution:
  def hourglassSum(self, arr):
    # minimun value
    maxS = -2^32
    # loop through columns
    for k in range(4):
      # loop even and odd rows 
      for j in range(2):
        i = j
        # sum row i
        vL1 = arr[i][k]+arr[i][k+1]+arr[i][k+2]
        while i + 2 <= 5:
          # sum row i+2
          vL3 = arr[i+2][k]+arr[i+2][k+1]+arr[i+2][k+2]
          # calculate hourglass sum
          vS = vL1 + vL3 + arr[i+1][k+1]
          # keep max value
          maxS = max([maxS, vS])
          # jump 2 rows
          i +=2
          # first new row is old 3 row...  alread summed as vL3
          vL1 = vL3
    # return max value
    return maxS
        

if __name__ == '__main__':
  s = Solution()
  arr = [[1,1,1,0,0,0],
			   [0,1,0,0,0,0],
			   [1,1,1,0,0,0],
			   [0,0,2,4,4,0],
			   [0,0,0,2,0,0],
			   [0,0,1,2,4,0]]
  print(s.hourglassSum(arr))

  arr = [[-1,-1, 0,-9,-2,-2],
			   [-2,-1,-6,-8,-2,-5],
			   [-1,-1,-1,-2,-3,-4],
			   [-1,-9,-2,-4,-4,-5],
			   [-7,-3,-3,-2,-9,-9],
			   [-1,-3,-1,-2,-4,-5]]
  print(s.hourglassSum(arr))