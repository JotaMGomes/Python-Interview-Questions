# https://leetcode.com/problems/fizz-buzz/
# Jose Luiz Mattos Gomes

from typing import List

class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
      # define return list
      vReturn = []
      # iteract from 1 to n
      for i in range(1, n+1):
        # test if is multiple of 3
        if i%3==0:
          # test if is also multiple of 5
          if i%5==0:
            vReturn.append('FizzBuzz')
          else:
            vReturn.append('Fizz')
        # test if is multiple of 5
        elif i%5==0:
          vReturn.append('Buzz')
        else:
          vReturn.append(str(i))

      # return final list
      return vReturn    


s = Solution()

print(s.fizzBuzz(15))
print(s.fizzBuzz(0))
print(s.fizzBuzz(75))