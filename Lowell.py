####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Chase'
strategy_name = 'Moral Jesus'
strategy_description = 'Be like jesus and forgive them. Always collude. If your points drop too low you lose faith in humanity and commit divine retribution and always betray.'
    
def move(my_history, their_history, my_score, their_score):
  '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
  # This player always colludes.
  if len(my_history) == 0:
    return "c"
  if (my_score >= 0) and (my_history[-1] == "c"):
      return "c"
  else:
    return "c"
  