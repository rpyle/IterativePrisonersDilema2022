####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'moyer'
strategy_name = 'Sacrifice3'
strategy_description = ':)'
  
import random
#state = 0
#lock = 0

def move(my_history, their_history, my_score, their_score):
  state = 0
  '''global lock
  if (len(my_history) == 0):
    pass
  elif ((their_history[0] == 'c') and (lock == 0)):
    lock = 1
  
  elif (lock == len(their_history)):
    
    if (their_history[1] == 'b' or 'c'):
      lock = 2
    if (their_history[2] == 'c' or 'b'):
      lock = 3
    if (their_history[3] == 'c' or 'b'):
      lock = 4
    if (their_history[4] == 'b' or 'c'):
      lock = 5
    if (their_history[5] == 'b' or 'c'):
      lock = 6
    if (their_history[6] == 'b' or 'c'):
      lock = 7
    if (their_history[7] == 'c' or 'b'):
      lock = 8
    if (their_history[8] == 'b' or 'c'):
      lock = 9
    if ((their_history[9] == 'c' or 'b') and (state == 0)):
      state = 2
  elif (len(their_history) < 10):
    pass
  elif (((their_history[1] == 'b') and (their_history[2] == 'c') and (their_history[3] == 'c') and (their_history[4] == 'b') and (their_history[5] == 'b') and (their_history[6] == 'b') and (their_history[7] == 'c') and (their_history[8] == 'b') and (their_history[9] == 'c') and (lock == 1)) or (their_history[1] == 'c' and their_history[2] == 'b' and their_history[3] == 'b' and their_history[4] == 'c' and their_history[5] == 'c' and their_history[6] == 'c' and their_history[7] == 'b' and their_history[8] == 'c' and their_history[9] == 'b' and lock == 1)):
    print('yes')
    state = 2
  else:
    state = 1'''

  if(len(my_history) < 10):
    pass
  elif (((their_history[0] == 'c') and (their_history[1] == 'b') and (their_history[2] == 'c') and (their_history[3] == 'c') and (their_history[4] == 'b') and (their_history[5] == 'b') and (their_history[6] == 'b') and (their_history[7] == 'c') and (their_history[8] == 'b') and (their_history[9] == 'c')) or (their_history[1] == 'c' and their_history[2] == 'b' and their_history[3] == 'b' and their_history[4] == 'c' and their_history[5] == 'c' and their_history[6] == 'c' and their_history[7] == 'b' and their_history[8] == 'c' and their_history[9] == 'b')):
    state = 2
  else:
    state = 1
  if (state == 1):
    #if 'b' in their_history[-20:]:
    #  return 'b'
    #else:
    #  return 'c'
    return 'b'
  elif (state == 2):
    return 'c'
  elif (state == 0):
    if (len(my_history) == 0):
      return 'b'
    if (len(my_history) == 1):
      return 'c'
    if (len(my_history) == 2):
      return 'b'
    if (len(my_history) == 3):
      return 'b'
    if (len(my_history) == 4):
      return 'c'
    if (len(my_history) == 5):
      return 'c'
    if (len(my_history) == 6):
      return 'c'
    if (len(my_history) == 7):
      return 'b'
    if (len(my_history) == 8):
      return 'c'
    if (len(my_history) == 9):
      return 'b'
  
    