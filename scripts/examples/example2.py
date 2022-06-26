
#https://codingbat.com/prob/p197466
def diff21(n):
  if n > 21:
    return abs(21-n) * 2
  else:
    return abs(21-n)

def diff21(n):
    return abs(21-n) * 2 if n> 21 else abs(21-n)
