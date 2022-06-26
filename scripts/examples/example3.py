#https://codingbat.com/prob/p166884

def parrot_trouble(talking, hour):
  if not talking:
    return False
  
  if hour < 7 or hour > 20:
    return True
  
  else:
    return False
    


def parrot_trouble(talking, hour): #=> 2^3 => 8 options
    pass
    # if talking and hour in range(0,7):

    # if talking and hour in range(7,21):
    
    # if talking and hour in range(8,23):
    #.. list all cases
    


def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)