# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, H:list)->int:
    numBlk = 0
    l = []
    for h in H:
      if len(l) == 0:
        l.append(h)
        continue

      if h == l[-1]:
        continue
      elif h > l[-1]:
        l.append(h) 
      else:
        while h < l[-1]:
          numBlk +=1
          l.pop()
          if len(l) == 0:
            break
        if len(l) > 0:
          if h != l[-1]:
            l.append(h)
        else:
          l.append(h)
    
    numBlk +=len(l)
    return numBlk

if __name__ == "__main__":
  s = Solution()
  print(s.s([8,8,5,7,9,8,7,4,8]))