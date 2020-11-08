# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
# Jose Luiz Mattos Gomes

class Solution:
  def s(self, A, B, K)->int:
    n = B // K 
    n = n - (A // K)
    if A % K == 0 and (A >= K or A == 0):
      n +=1

    return n


if __name__ == '__main__':
  s = Solution()
  print(s.s(6,11,2))
  print(s.s(11,345,17))
  print(s.s(0,0,11))