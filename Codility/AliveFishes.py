# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, A:List, B:List)->int:
    i = 0
    alive = 0
    upstream = []
    while i < len(B):
      
      if B[i] == 0:
        # downstream
        while len(upstream) > 0:
          if A[i] > upstream[len(upstream)-1]:
            upstream.pop()
          else:
            break
        
        if len(upstream) == 0:
          alive +=1
      
      else:
        # upstream
        upstream.append(A[i])

      i +=1
    
    alive += len(upstream)
    return alive



if __name__ == "__main__":
  s = Solution()
  print(s.s([4,3,2,1,5],[0,1,0,0,0]))