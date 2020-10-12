# Jose Luiz Mattos Gomes

class Solution:
  def s(self, A):
    i = 1
    
    if A[0] == 'a':
      while i < len(A) and A[i] == 'a':
        i +=1
      if i >= len(A):
        return True
    
    while i < len(A) and A[i] == 'b':
      i +=1

    if i >= len(A):
      return True
    return False
           


if __name__ == '__main__':
  s = Solution()
  print(s.s("b"))
  print(s.s("ab"))
  print(s.s("aabb"))
  print(s.s("aabab"))
  print(s.s("bb"))
  print(s.s("bba"))
  print(s.s("ba"))
