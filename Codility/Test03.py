# Jose Luiz Mattos Gomes

class Solution:
  def solution(self, A)-> int:
    i = 0
    cnt = 0
    tr = list()

    def test3(t1, t2, t3):
      return (A[t1] > A[t2] and A[t2] < A[t3]) or (A[t1] < A[t2] and A[t2] > A[t3])
    
    # the main idea is to compare trees 3 by 3
    while i < len(A) -2:
      if not test3(i, i+1, i+2):
        # store the 3 possible trees that can be removed
        tr.append(i)
        tr.append(i+1)
        tr.append(i+2)

      if len(tr) > 3:
        # more than 1 tree need to be removed
        return -1

      i+=1

    if len(tr) == 0:
      return 0

    canRemove = True
    for i in tr:
      if i-2 > 0 and i+1< len(A):
        canRemove = canRemove and test3(i-2, i-1, i+1)
      if i-1 > 0 and i+2< len(A):
        canRemove = canRemove and test3(i-1, i+1, i+2)        

      if canRemove:
        cnt+=1

    if cnt == 0:
      cnt = -1

    return cnt
               
if __name__ == '__main__':
  s = Solution()
  print(s.solution([3, 4, 5, 3, 7]))
  print(s.solution([1, 2, 3, 4]))
  print(s.solution([1, 3, 1, 2]))
  print(s.solution([4, 4, 4, 5, 3]))