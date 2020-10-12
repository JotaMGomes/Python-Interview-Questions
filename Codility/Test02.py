# Jose Luiz Mattos Gomes

class Solution:
  def s(self, N) -> int:
    v = str(N)
    i = 0
    if N > 0:
      while i < len(v):
        if v[i] > '5':
          i +=1
        else:
          return int(v[:i]+'5'+v[i:])
      return int(v+'5')
    else:
      while i < len(v):
        if v[i] < '5':
          i +=1
        else:
          return int(v[:i]+'5'+v[i:])
      return int(v+'5')      


if __name__ == '__main__':
  s = Solution()
  print(s.s(268))
  print(s.s(670))
  print(s.s(5260))
  print(s.s(50))
  print(s.s(-999))
  print(s.s(999))
  print(s.s(0))
  print(s.s(-5999))
  print(s.s(-1))
  print(s.s(1))
  print(s.s(88221))
  print(s.s(-161))
  print(s.s(-151)) 