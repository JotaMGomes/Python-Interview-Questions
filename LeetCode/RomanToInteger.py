# https://leetcode.com/problems/roman-to-integer/
# Jose Luiz Mattos Gomes

class Solution:
  def romanToInt(self, s: str) -> int:
    # define dictionary with symbols values
    rateDic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    # define string with roman sequence symbols
    romanNumSequence = 'IVXLCDM'
    # define accumulator
    vReturn = 0
    
    # iteract through string chars
    i = 0
    while i<len(s):
      # define aux variable to store current value symbol
      auxValue = rateDic.get(s[i])
      # test if symbol is valid
      if auxValue == None:
        # invalid Roman number
        return 0
      
      if i<len(s)-1:
        # test next value
        
        # if next value is less than current value,
    		#    subtract current value from last value
        if rateDic.get(s[i+1]) != None:
          if auxValue < rateDic.get(s[i+1]):
            if romanNumSequence.index(s[i+1]) - romanNumSequence.index(s[i]) > 2:
              # invalid Roman number
              # You can only subtract from the next two higher "digits." 
              return 0
              
            # update current value
            auxValue = rateDic.get(s[i+1]) - auxValue
            # update index
            i+=1

      # update accumulator
      vReturn += auxValue
      # update index
      i+=1
    
    # return found value
    return vReturn


s = Solution()

print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("IX"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("y"))
print(s.romanToInt("IM"))
print(s.romanToInt("Iy"))