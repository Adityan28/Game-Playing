# Name: G Adityan
# ID: 2016B1A70929P

import minimax_pruning, board
import time

# PLAYER H is mentioned as 1.
# PLAYER M is mentioned as 2.
# Not all function names match as given in the PDF for the Assignment. 

# PLAYING THE GAME USING ALPHA BETA PRUNING ONCE TO DEPICT THE GRAPHICS
# (Don't Close the Window displaying the game)
# (Carry on with the rest of the program)
# (Finally, close the window displaying the game)
minimax_pruning.run_ab_pruning()
board.graphics_function()

# PLAY THE GAME USING BOTH MINIMAX AND ALPHA BETA PRUNING FOR ALL THE DETAILS(R1-R9) 
minimax_pruning.playboth()

# PLAYING THE GAME 10 TIMES USING ALPHA BETA PRUNING
start = time.time()
num_m_wins = 0
for i in range(2):
    num_m_wins += minimax_pruning.run_ab_pruning()
end = time.time()
time_taken = end-start
average_time = time_taken/2
print("Total time for 10 games: ", time_taken)
print("Average time for 10 games: ", average_time)
print("Number of times M won: ", num_m_wins)


# PLAYING THE GAME 20 TIMES USING ALPHA BETA PRUNING
start = time.time()
num_m_wins = 0
for i in range(3):
    num_m_wins += minimax_pruning.run_ab_pruning()
end = time.time()
time_taken = end-start
average_time = time_taken/3
print("Total time for 20 games: ", time_taken)
print("Average time for 20 games: ", average_time)
print("Number of times M won: ", num_m_wins)

