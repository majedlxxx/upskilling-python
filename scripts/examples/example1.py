#https://codingbat.com/prob/p173401

def sleep_in(weekday, vacation):
    if weekday and not vacation:
        return False
    else:
        return True
def sleep_in(weekday, vacation):
  return vacation or not weekday
  
test_cases = [
    (True, True),
    (True, False),
    (False, True),
    (False, False)
]

print("Weekday, vacation")
for t in test_cases:
    print(f"{t} => {sleep_in(t[0], t[1])}")

def abs(n):
    if n>=0:
        return n
    else:
        return n*-1