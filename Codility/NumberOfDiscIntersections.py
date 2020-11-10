# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
# Jose Luiz Mattos Gomes

from typing import List

#not right

class Solution:
  def s(self, A:List)->int:
    i = 0
    acc = 0
    while i < len(A):
      j = i + 1
      l1 = i - A[i]
      r1= i + A[i]
      while j < len(A):
        l2 = j - A[j]
        r2 = j + A[j] 
        if (l2 >= l1) and (l2 <= r1) or (r2 >= l1) and (r2 <= r1) or (l1 >= l2) and (l1 <= r2) or (r1 >= l2) and (r1 <= r2) :
          acc +=1
          if acc > 10000000:
            return -1
        j +=1
      i +=1
    return acc


  def s1(self, A:List)->int:
    i = 0
    acc = 0
    A2 = []
    while i < len(A):
      l1 = i - A[i]
      A2.append([l1, i])
      A2.sort()
      i +=1
    
    i = 0
    while i < len(A2):
      j = i + 1
      right = 2 * A2[i][1] - A2[i][0]
      while j < len(A2) and A2[j][0] <= right:
        acc +=1
        if acc > 10000000:
          return -1
        j +=1 
      i +=1

    return acc


  def s2(self, A:List)->int:
    # find left and right points
    A2 = [[i-j,i+j] for i,j in enumerate(A)]
    # sort by left
    A2.sort()
    i = 0
    discOpen = [] # keep all circles with right > current left
    acc = 0
    while i < len(A2):
      j = 0
      while j < len(discOpen):
        if A2[i][0] > discOpen[j]:
          # remove circles that right is > than current left
          discOpen.remove(discOpen[j])
        else:
          j+=1
      
      acc += len(discOpen)
      if acc > 10000000:
        return -1

      discOpen.append(A2[i][1])
      i +=1

    return acc      


if __name__ == "__main__":
  s = Solution()
  print(s.s([1,5,2,1,4,0]))
  print(s.s([1,1,1]))
  print("===")
  print(s.s1([1,5,2,1,4,0]))
  print(s.s1([1,1,1]))
  print("===")
  print(s.s2([1,5,2,1,4,0]))
  print(s.s2([1,1,1]))  
  