    ####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'moyer'
strategy_name = 'Malice'
strategy_description = 'Collude but retaliate.'
  
import random

def move(my_history, their_history, my_score, their_score):
    
    if 'b' in their_history[-20:]:
      return 'b'
    else:
      return 'c'
    
    '''if len(my_history) == 0:
      return 'c'
    else:
      if their_history[-1] == 'b':
        return 'b'
      elif their_history[-1] == 'c':
        return 'c'''
      