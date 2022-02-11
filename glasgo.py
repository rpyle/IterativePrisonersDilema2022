####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Glasgo'
strategy_name = "Disgustingly metagame"
strategy_description = 'Always never betray.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    

		#step 1: determine what strategy is being employed
		#step 2: employ the best action against that strategy
		#step 3: if unable to determine strategy, go tit-for-tat
		#step 4: if mod 69 is 0, pick random



    #This example player always betrays.      
    return 'b'
