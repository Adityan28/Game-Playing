# Name: G Adityan
# ID: 2016B1A70929P

import board
import pickle
import time
import sys

moves_list = []

class AIGame:
    def __init__(self):
        self.reset_aigame()

    def reset_aigame(self):
        self.current_state = [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]
        self.turn = '1'

    def is_valid(self, px, py):
        if px<0 or px>3 or py<0 or py>3:
            return False
        elif self.current_state[px][py] != '-':
            return False
        else:
            for i in range(px):
                if self.current_state[i][py] == '-':
                    return False
            return True

    # Not Necessary. Just for clarity.
    def draw_board(self):
        for i in range(4):
            for j in range(4):
                print('{}|'.format(self.current_state[i][j]), end = " ")
            print()
        print()

    def Terminal_Test(self):
        # Condition for Horizontal Win
        for i in range(0, 4):
            if self.current_state[i][0]!='-' and self.current_state[i][0]==self.current_state[i][1] and self.current_state[i][1]==self.current_state[i][2]:
                return self.current_state[i][0]
            elif self.current_state[i][1]!='-' and self.current_state[i][1]==self.current_state[i][2] and self.current_state[i][2]==self.current_state[i][3]:
                return self.current_state[i][1]

        # Condition for Vertical Win    
        for i in range(0, 4):
            if self.current_state[0][i] != '-' and self.current_state[0][i] == self.current_state[1][i] and self.current_state[1][i] == self.current_state[2][i]:
                return self.current_state[0][i]
            elif self.current_state[1][i] != '-' and self.current_state[1][i] == self.current_state[2][i] and self.current_state[2][i] == self.current_state[3][i]:
                return self.current_state[1][i]


        # Condition for Diagonal Win
        if (self.current_state[0][0] != '-' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]
        elif (self.current_state[1][1] != '-' and
            self.current_state[1][1] == self.current_state[2][2] and
            self.current_state[1][1] == self.current_state[3][3]):
            return self.current_state[1][1]
        elif (self.current_state[1][0] != '-' and
            self.current_state[1][0] == self.current_state[2][1] and
            self.current_state[1][0] == self.current_state[3][2]):
            return self.current_state[1][0]
        elif (self.current_state[0][1] != '-' and
            self.current_state[0][1] == self.current_state[1][2] and
            self.current_state[0][1] == self.current_state[2][3]):
            return self.current_state[0][1]
        

        elif (self.current_state[0][3] != '-' and
            self.current_state[0][3] == self.current_state[1][2] and
            self.current_state[0][3] == self.current_state[2][1]):
            return self.current_state[0][3]
        elif (self.current_state[1][2] != '-' and
            self.current_state[1][2] == self.current_state[2][1] and
            self.current_state[1][2] == self.current_state[3][0]):
            return self.current_state[1][2]
        elif (self.current_state[0][2] != '-' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]
        elif (self.current_state[1][3] != '-' and
            self.current_state[1][3] == self.current_state[2][2] and
            self.current_state[1][3] == self.current_state[3][1]):
            return self.current_state[1][3]

        # Checking for empty spaces in the board
        for i in range(0, 4):
            for j in range(0, 4):
                if (self.current_state[i][j] == '-'):
                    return None

        # Game is Tied
        return '-'



    def max(self, count):

        maxv = -100000
        px = None
        py = None

        result = self.Terminal_Test()
        if result == '1':
            return (-1, 0, 0,count)
        elif result == '2':
            return (1, 0, 0,count)
        elif result == '-':
            return (0, 0, 0,count)


        for i in range(0, 4):
            k=0
            while k<4 and self.current_state[k][i]!='-':
                k+=1
            if k<4:
                count += 1
                self.current_state[k][i] = '2'
                (m, min_i, min_j, count) = self.min(count)
                if m > maxv:
                    maxv = m
                    px = k
                    py = i
                self.current_state[k][i] = '-'
            else:
                continue
        return (maxv, px, py, count)

    def min(self, count):
        minv = 2
        qx = None
        qy = None

        result = self.Terminal_Test()
        if result == '1':
            return (-1, 0, 0,count)
        elif result == '2':
            return (1, 0, 0,count)
        elif result == '-':
            return (0, 0, 0,count)


        for i in range(0, 4):
            k=0
            while k<4 and self.current_state[k][i]!='-':
                k+=1
            if k<4:
                count += 1
                self.current_state[k][i] = '1'
                (m, min_i, min_j, count) = self.max(count)
                if m < minv:
                    minv = m
                    qx = k
                    qy = i
                self.current_state[k][i] = '-'
            else:
                continue

        return (minv, qx, qy, count)



    def max_alpha_beta(self, alpha, beta, count):
        maxv = -2
        px = None
        py = None

        result = self.Terminal_Test()
        if result == '1':
            return (-1, 0, 0,count)
        elif result == '2':
            return (1, 0, 0,count)
        elif result == '-':
            return (0, 0, 0,count)


        for i in range(0, 4):
            k=0
            while k<4 and self.current_state[k][i]!='-':
                k+=1
            if k<4:
                count += 1
                self.current_state[k][i] = '2'
                (m, min_i, min_j, count) = self.min_alpha_beta(alpha, beta, count)
                if m > maxv:
                    maxv = m
                    px = k
                    py = i
                self.current_state[k][i] = '-'
                if maxv >= beta:
                        return (maxv, px, py, count)

                if maxv > alpha:
                    alpha = maxv
            else:
                continue

        return (maxv, px, py, count)


    def min_alpha_beta(self, alpha, beta, count):
        minv = 2
        qx = None
        qy = None

        result = self.Terminal_Test()
        if result == '1':
            return (-1, 0, 0,count)
        elif result == '2':
            return (1, 0, 0,count)
        elif result == '-':
            return (0, 0, 0,count)


        for i in range(0, 4):
            k=0
            while k<4 and self.current_state[k][i]!='-':
                k+=1
            if k<4:
                count += 1
                self.current_state[k][i] = '1'
                (m, max_i, max_j, count) = self.max_alpha_beta(alpha, beta, count)
                if m < minv:
                    minv = m
                    qx = k
                    qy = i
                self.current_state[k][i] = '-'
                if minv <= alpha:
                        return (minv, qx, qy, count)

                if minv < beta:
                    beta = minv
            else:
                continue

        return (minv, qx, qy, count)



    def play_alpha_beta(self):
        players_count = 0
        ais_count = 0
        num_nodes = 0
        total_time_start = time.time()
        total_time_end = 0
        while True:
            self.draw_board()
            self.result = self.Terminal_Test()
            if self.result != None:
                if self.result == '1':
                    print('The winner is 1!')
                elif self.result == '2':
                    print('The winner is 2!')
                elif self.result == '-':
                    print("It's a tie!")
                total_time_end = time.time()
                total_time_taken = total_time_end - total_time_start
                self.reset_aigame()
                #print("ALL THE MOVES:\n\n")
                #print(moves_list)
                fp = open("moves_list.pkl", "wb")
                pickle.dump(moves_list, fp)
                fp.close()
                num_nodes = players_count + ais_count
                print("Number of nodes generated: ", num_nodes)
                sizeof_oneentry = sys.getsizeof('-')
                print("Memory allocated to 1 node (in bytes): ", sizeof_oneentry*16)
                print("Total memory used by ALPHA-BETA PRUNING Algorithm (in bytes): ", num_nodes*sizeof_oneentry*16)
                print("Number of nodes generated in 1 micro second: ", num_nodes/(total_time_taken*(10**6)))
                print("Total time taken for the game(in seconds): ",total_time_taken)
                return (num_nodes, total_time_taken, self.result)

            if self.turn == '1':

                while True:
                    
                    start = time.time()
                    print("Start time: ", start)
                    (m, qx, qy, players_count) = self.min_alpha_beta(-2, 2, players_count)
                    end = time.time()
                    print("End time: ", end)
                    print('Evaluation time: {}s'.format(round(end - start, 7)))

                    px = int(input('Enter the Row Number: '))
                    py = int(input('Enter the Column Number: '))
                    qx = px
                    qy = py

                    if self.is_valid(px, py):
                        self.current_state[px][py] = '1'
                        moves_list.append([px,py])
                        #print("PLAYER's COUNT HERE: ", players_count)
                        self.turn = '2'
                        break
                    else:
                        print('The move is not valid! Try again.')

            else:
                
                (m, px, py, ais_count) = self.max_alpha_beta(-2, 2, ais_count)
                self.current_state[px][py] = '2'
                moves_list.append([px,py])
                #print("AI's COUNT HERE: ", ais_count)
                self.turn = '1'

    def play(self):
        players_count = 0
        ais_count = 0
        num_nodes = 0
        total_time_start = time.time()
        total_time_end = 0
        while True:
            self.draw_board()
            self.result = self.Terminal_Test()

            if self.result != None:
                if self.result == '1':
                    print('The winner is 1!')
                elif self.result == '2':
                    print('The winner is 2!')
                elif self.result == '-':
                    print("It's a tie!")

                total_time_end = time.time()
                total_time_taken = total_time_end - total_time_start
                self.reset_aigame()
                #print("ALL THE MOVES:\n\n")
                #print(moves_list)
                fp = open("moves_list.pkl", "wb")
                pickle.dump(moves_list, fp)
                fp.close()
                num_nodes = players_count + ais_count
                print("Number of nodes generated: ", num_nodes)
                sizeof_oneentry = sys.getsizeof('-')
                print("Memory allocated to 1 node (in bytes): ", sizeof_oneentry*16)
                print("Total memory used by MINIMAX Algorithm (in bytes): ", num_nodes*sizeof_oneentry*16)
                print("Number of nodes generated in 1 micro second: ", num_nodes/(total_time_taken*(10**6)))
                print("Total time taken for the game(in seconds): ",total_time_taken)
                return (num_nodes, total_time_taken, self.result)

            
            if self.turn == '1':

                while True:
                    
                    start = time.time()
                    print("Start time: ", start)
                    (m, qx, qy, players_count) = self.min(players_count)
                    end = time.time()
                    print("End time: ", end)
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    
                    px = int(input('Enter the Row Number: '))
                    py = int(input('Enter the Column Number: '))
                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = '1'
                        moves_list.append([px,py])
                        #print("PLAYER's COUNT HERE: ", players_count)
                        self.turn = '2'
                        break
                    else:
                        print('The move is not valid! Try again.')

            
            else:
                
                (m, px, py, ais_count) = self.max(ais_count)
                self.current_state[px][py] = '2'
                moves_list.append([px,py])
                #print("AI's COUNT HERE: ", ais_count)
                self.turn = '1'

def playboth():
    g = AIGame()
    print("\nPLAYING USING ALPHA BETA PRUNING:\n")
    ab = g.play_alpha_beta()
    print("\nPLAYING USING MINIMAX PRUNING:\n")
    mm = g.play()
    r1 = ab[0]
    r6 = mm[0]
    print("(R1-R6)/R1 : ", (r1-r6)/r1)
    print("Ratio of time taken by Minimax algorithm to Alpha beta pruning: ", mm[1]/ab[1])
    print("Ratio of memory consumed by Minimax to that of Alpha beta pruning: ", r6/r1)

def run_minimax():
    g = AIGame()
    ab = g.play()

def run_ab_pruning():
    g = AIGame()
    ab = g.play_alpha_beta()
    if ab[2] == '2':
        return 1
    return 0
