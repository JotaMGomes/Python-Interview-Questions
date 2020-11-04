# https://www.careercup.com/question?id=21263687
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def s(self, vl:List) -> List:
    vi = [0] * len(vl)
    for l in vl:
      vi[l-1]+=1

    i = 0
    while i < len(vi):
      print('Elem: ' + str(i+1) + ' Count: ' + str(vi[i]))
      i +=1
    


if __name__ == '__main__':
  s = Solution()
  s.s([6,1,5,6,6,4])