####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'moyer'
strategy_name = 'Malice'
strategy_description = ':)'
  
import random
round = 0
state = 0
lock = 0

def move(my_history, their_history, my_score, their_score):
  global round
  global state
  global lock
  try:
    if(my_history[round - 1]):
      pass
  except IndexError:
    round = 0
    lock = 0
    state = 0

  if (len(my_history) == 0):
    #state = 0
    pass
  elif (their_history[0] == 'b' and lock == 0):
    lock = 1
  
  elif (lock == len(their_history) + 1):
    if (their_history[1] == 'c'):
      lock = 2
    if (their_history[2] == 'b'):
      lock = 3
    if (their_history[3] == 'b'):
      lock = 4
    if (their_history[4] == 'c'):
      lock = 5
    if (their_history[5] == 'c'):
      lock = 6
    if (their_history[6] == 'c'):
      lock = 7
    if (their_history[7] == 'b'):
      lock = 8
    if (their_history[8] == 'c'):
      lock = 9
    if ((their_history[9] == 'b') and (state == 0)):

      state = 2

  else:
   state = 1

  if (round == 0):
    pass
  elif (round < 10):
    print(my_history[round - 1])
  
  round = round + 1

  if (state == 1):
    if 'b' in their_history[-20:]:
      return 'b'
    else:
      return 'c'
  elif (state == 2):
    return 'b'
  elif (state == 0):
    '''if (len(their_history) == 0):
      return 'c'
    if (len(their_history) == 1):
      return 'b'
    if (len(their_history) == 2):
      return 'c'
    if (len(their_history) == 3):
      return 'c'
    if (len(their_history) == 4):
      return 'b'
    if (len(their_history) == 5):
      return 'b'
    if (len(their_history) == 6):
      return 'b'
    if (len(their_history) == 7):
      return 'c'
    if (len(their_history) == 8):
      return 'b'
    if (len(their_history) == 9):
      return 'c'''
    if (round == 1):
      return 'c'
    if (round == 2):
      return 'b'
    if (round == 3):
      return 'c'
    if (round == 4):
      return 'c'
    if (round == 5):
      return 'b'
    if (round == 6):
      return 'b'
    if (round == 7):
      return 'b'
    if (round == 8):
      return 'c'
    if (round == 9):
      return 'b'
    if (round == 10):
      return 'c'
    
    