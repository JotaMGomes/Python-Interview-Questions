# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# Jose Luiz Mattos Gomes


class Solution:
  def solution(self, A) -> int:
    # define return variable as max value possible
    vMinDiff = 2**32
    
    # first summ all values and keep it into vAcc1
    vAcc1 = sum(A)
    # define second accumulator as 0	
    vAcc2 = 0
    # iteract through list 
    for i in range(len(A)-1):
      # update accumulator with next number
      vAcc2 += A[i]
      # verify differences 
      if abs(vAcc2 - (vAcc1 - vAcc2)) < vMinDiff:
        # found a minimun sum, so keep it into vMinDiff
        vMinDiff = abs(vAcc2 - (vAcc1 - vAcc2))

    # return vMinDiff
    return vMinDiff


s = Solution()

vList = [3,1,2,4,3]
print(s.solution(vList))

vList = [3, 3]
print(s.solution(vList))
