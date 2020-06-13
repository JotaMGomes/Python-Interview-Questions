# https://leetcode.com/problems/count-primes/
# Jose Luiz Mattos Gomes

class Solution:
  def countPrimes(self, n: int) -> int:
    """
    When a number is not a prime, this number can be factored into two factors namely a and b 
    i.e. number = a * b. 
    If both a and b were greater than the square root of n, a * b would be greater than n.
    """
    # test if number is less than 2
    if n<=2:
      return 0
    
    # define list of prime numbers
    self.primeList = [2]

    # interact from 3 to n, step 2
    for i in range(3, n, 2):
      # test if i is prime
      self.isPrime(i)
    
    # return number of items in primeList
    return len(self.primeList)


  # function to verify is number is prime
  def isPrime(self, number: int):
    # iteract items on primeList
    for i in self.primeList:
      # leave loop if i*i > number
      if i*i > number:
        break
      # if the remainder is zero than is not prime
      if number % i == 0: 
        return

    # increment i
    i +=1
    # iteract from i to i**2
    while i*i <= number:
      # if the remainder is zero than is not prime
      if number % i == 0: 
        return 
      # update i
      i+=2

    # number is a prime number, add to primeList
    self.primeList.append(number)
    return     

s = Solution()

print(s.countPrimes(499979))
print(s.countPrimes(999983))

print(s.countPrimes(3))
print(s.countPrimes(10))
print(s.countPrimes(99))