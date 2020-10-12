# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
# Jose Luiz Mattos Gomes

class Solution:
  def solution(self, A):
    # sort list
    A.sort()
    # test first 3 with last 3 elements
    return max([A[ 0]*A[ 1]*A[ 2], 
                A[ 0]*A[ 1]*A[-1],
                A[ 0]*A[-1]*A[-2],
                A[-3]*A[-2]*A[-1]])   


if __name__ == '__main__':
  s = Solution()
  print(s.solution([-3,1,2,2,-2,5,6]))
  print(s.solution([-5,5,-5,4]))