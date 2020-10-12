# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
# Jose Luiz Mattos Gomes

class Solution:
  def s(self, A) -> int:
    A.sort()
    i = 0
    while i < len(A):
      if A[i] != i+1:
        return 0
      i +=1
    return 1


if __name__ == '__main__':
  s = Solution()
  print(s.s([4,1,3,2]))
  print(s.s([4,1,3]))
  print(s.s([4,1,3,2,2]))
  print(s.s([1]))
