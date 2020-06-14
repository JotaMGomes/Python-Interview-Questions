# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# Jose Luiz Mattos Gomes


class Solution:
  def solution(self, X, Y, D) -> int:
    # calculate number of jumps
    numJumps = (Y - X) // D
    if (Y - X) % D > 0:
      # add 1 jump if remainder is bigger than 0
      numJumps +=1

    # return number of jumps
    return numJumps


s = Solution()

print(s.solution(10, 85, 30))
