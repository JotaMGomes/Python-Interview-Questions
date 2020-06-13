# https://leetcode.com/problems/combinations/
# Jose Luiz Mattos Gomes

from typing import List
from itertools import combinations

class Solution:

    ###############################################
    # solution using combinations library
    def combine(self, n: int, k: int) -> List[List[int]]:
      # define rList as the result variable
      self.rList : List[List[int]] = list(list())

      # create a 1-n list
      self.nList = [*range(1,n+1)]
      
      # generate all n choose k combinations
      cmb = combinations(self.nList, k)
      
      # iterate from all combinations 
      for c in cmb:
        # add the combination to rList as a list
        self.rList.append(list(c))
      
      # return rList
      return self.rList

    ###############################################
    # recursive solution
    # main function
    def rec1(self, n:int, k:int) -> List[List[int]]:
      # define rList as the result variable
      self.rList : List[List[int]] = list(list())

      # create a 1-n list
      self.nList = [*range(1,n+1)]

      # update class variables
      self.n = n
      self.k = k
      # print(self.nList)

      # iterate from 1 to n-k+1
      for i in range(n-k+1):
        # call recursive function
        self.rec2(list(), i)

      # return rList
      return self.rList
      
    
    
    # recursive function
    def rec2(self, xList : List[int], p:int): 
      # add p to xList
      xList.append(self.nList[p])
      
      # if len(xList)==k then add current list to rList and exit
      if len(xList)==self.k:
        self.rList.append(xList.copy())
        return

      # while p < n-1 call the recursive function again
      #  with a copy of xList and the next value of p
      while p<self.n-1:
        self.rec2(xList.copy(), p+1)
        p+=1
      
      # exit recursive function
      return


s = Solution()
print(s.combine(4,2))
print(s.rec1(4,2))
print("======")
print(s.combine(5,1))
print(s.rec1(5,1))
print("======")
print(s.combine(5,2))
print(s.rec1(5,2))
print("======")
print(s.combine(5,3))
print(s.rec1(5,3))
print("======")
print(s.combine(5,4))
print(s.rec1(5,4))
print("======")
print(s.combine(5,5))
print(s.rec1(5,5))