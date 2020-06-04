# https://leetcode.com/problems/bulls-and-cows/

class Solution:
  def getHint(self, secret: str, guess: str) -> str:
    # define lists to keep char positions
    bull = []
    cow  = []

    # iteract through chars of secret
    for p in range(len(secret)):
      # test is there is a match in char position
      if secret[p] == guess[p]:
        # char found at the right position: add bull list
        bull.append(p)
      else:
        # try to find char secret[p] in guess
        i = guess.find(secret[p])
        if i > -1:
          # verity if this the position found is already in bull, cow, or if there is a match char in that position
          findNext = (i in bull) or (i in cow) or (secret[i] == guess[i])
          if findNext:
            # keep looking for another position for the same char
            while findNext:
              i = guess.find(secret[p],i+1)
              if i > -1:
                findNext = (i in bull) or (i in cow) or (secret[i] == guess[i])
                if not findNext:
                  # char found, but in wrong position: add cow list
                  cow.append(i)
              else:
                # char not found
                findNext = False
          else:
            # char found, but in wrong position: add cow list
            cow.append(i)
    # return final string
    return(str(len(bull))+"A"+str(len(cow))+"B")
 


s = Solution()

print(s.getHint("1122", "2211"))
print(s.getHint("1807", "7810"))
print(s.getHint("1123", "0111"))
print(s.getHint("1122", "0001"))