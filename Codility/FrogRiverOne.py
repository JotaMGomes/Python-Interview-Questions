# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# Jose Luiz Mattos Gomes


class Solution:
  def solution(self, X, A) -> int:
    # create an empty set
    vSet = set()
    # iteract through A
    # define counter
    vPointer = 0
    for i in A:
      # add i to vSet
      vSet.add(i)
      # test if size vSet = X
      if len(vSet)==X:
          # return counter
          return vPointer
      vPointer+=1

    # no possible solution, return -1
    return -1


s = Solution()

iList = [1,3,1,4,2,3,5,4]
K = 5
print(s.solution(K, iList))
