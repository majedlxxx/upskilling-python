#https://codingbat.com/prob/p118406
from matplotlib.style import available


def make_bricks(small, big, goal):
    if goal < 5: # 4
        return small >= goal

    collected = 0
    big_bricks_needed = int(goal/5) # 1
    if big >= big_bricks_needed:
        collected += 5 * big_bricks_needed
    else:
        collected += 5 * big
        
    small_needed = goal - collected
    
    if small >= small_needed:
        return True
    else:
        return False
    



def make_bricks(small, big, goal):
    if goal < 5: # 4
        return small >= goal
    
    big_bricks_needed = int(goal/5) # 1
    if big >= big_bricks_needed:
        goal -= 5 * big_bricks_needed
    else:
        goal -= 5 * big
  
    return small >= goal
    # if small >= goal:
    #     return True
    # else:
    #     return False

def make_bricks(small, big, goal):
    if goal < 5: # 4
        return small >= goal
    big_bricks_needed = int(goal/5) # 1
    goal = goal - 5 * big_bricks_needed if big >= big_bricks_needed else goal - 5 * big
    return small >= goal


def make_bricks(small, big, goal):
    if goal < 5: # 4
        return small >= goal
    big_bricks_needed = int(goal/5) # 1
    goal -= min(big, big_bricks_needed) * 5
    return small >= goal


def withdraw_from_atm(available, amount):
    # return True of False
    pass


available = {
    5: 5, # 5 * 5$
    10: 2, #2 * 10$
    1: 3,
}
available = {
    5: 5,
    10: 2,
    1: 3,
    20: 3,
    50: 30,
}

available_bills = sorted(available.keys())