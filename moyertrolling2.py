####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'moyer'
strategy_name = 'Sacrifice2'
strategy_description = ':)'
  
import random
round = 0
state = 0

def move(my_history, their_history, my_score, their_score):
  global round
  global state
  try:
    if(my_history[round - 1]):
      pass
  except IndexError:
    round = 0
    state = 0
  

  if (state == 1):
    #if 'b' in their_history[-20:]:
    #  return 'b'
    #else:
    #  return 'c'
    return 'b'
  elif (state == 2):
    return 'c'
  elif (state == 0):
    if (round == 1):
      return 'b'
    if (round == 2):
      return 'c'
    if (round == 3):
      return 'b'
    if (round == 4):
      return 'b'
    if (round == 5):
      return 'c'
    if (round == 6):
      return 'c'
    if (round == 7):
      return 'c'
    if (round == 8):
      return 'b'
    if (round == 9):
      return 'c'
    if (round == 10):
      return 'b'
    