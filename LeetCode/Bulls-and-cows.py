# https://leetcode.com/problems/bulls-and-cows/

from typing import List

class Solution:
  def getHint(self, secret: str, guess: str) -> str:
    bull = []
    cow  = []
    p = 0
    for p in range(len(secret)):
      if secret[p] == guess[p]:
        bull.append(p)
      else:
        i = guess.find(secret[p])
        if i > -1:
          findNext = (i in bull) or (i in cow) or (secret[i] == guess[i])
          if findNext:
            while findNext:
              i = guess.find(secret[p],i+1)
              if i > -1:
                findNext = (i in bull) or (i in cow) or (secret[i] == guess[i])
                if not findNext:
                  cow.append(i)
              else:
                findNext = False
          else:
            cow.append(i)

    return(str(len(bull))+"A"+str(len(cow))+"B")
 


s = Solution()

print(s.getHint("1122", "2211"))
print(s.getHint("1807", "7810"))
print(s.getHint("1123", "0111"))
print(s.getHint("1122", "0001"))