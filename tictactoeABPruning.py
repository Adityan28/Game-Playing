import math

global cnt

size = 3
ai, human = 1, 2
scores = {1: 5, 2: -1,0: 0}
currentPlayer = ai

board = [[0 for i in range(size)] for j in range(size)]

for i in range(size):
    for j in range(size):
        print(board[i][j]," ")

def equals(x,y,z):
    return x==y and y==z and x!=0

def checkWinner():
    winner = None
    # horizontal
    for i in range(size):
        if equals(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]

    #vertical
    for i in range(size):
        if equals(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]

    if equals(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]

    if equals(board[0][2], board[1][1], board[2][0]):
        winner = board[0][2]

    return winner

def minimax(board, depth, isMaximizing, alpha, beta):
    result = checkWinner()
    global cnt
    cnt+=1
    if result !=None:
        #print("Depth: ", depth)
        return scores[result]
    
    if(isMaximizing):
        bestScore = -math.inf
        for i in range(size):
            for j in range(size):
                if board[i][j] == 0:
                    #print("ai: ", ai)
                    board[i][j] = ai
                    score = minimax(board, depth+1, False, alpha, beta)
                    board[i][j] = 0
                    bestScore = max(bestScore, score)
                    if bestScore >= beta:
                        return bestScore
                    alpha = max(alpha, bestScore)
        return bestScore
    
    else:
        bestScore = math.inf
        for i in range(size):
            for j in range(size):
                if board[i][j] == 0:
                    #print("human: ", human)
                    board[i][j] = human
                    score = minimax(board, depth+1, True, alpha, beta)
                    board[i][j] = 0
                    bestScore = min(bestScore, score)
                    if bestScore <= alpha:
                        return bestScore
                    beta = min(beta, bestScore)
        return bestScore

def bestMove():
    bestScore = -math.inf
    global cnt
    cnt=0
    move=[]
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                board[i][j] = ai
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = 0
                print("Score: ", score, "and cnt: ", cnt)
                if score>bestScore:
                    bestScore = score
                    move = [i, j]
    board[move[0]][move[1]] = ai
    currentPlayer = 2
    return currentPlayer

def printBoard():
    print("\nCurrent State of Board")
    for i in range(size):
        for j in range(size):
            print(board[i][j], end=' ')
        print("\n")

def main():
    emptySpaces = 9
    while True:
        print("AI move")
        currentPlayer = bestMove()
        emptySpaces -= 1
        printBoard()
        over = checkWinner()
        if over != None:
            print("\n***GAME OVER***\n")
            printBoard()
            print("AI Wins!")
            break
        if emptySpaces==0:
            print("Game Tied!")
            break
        while currentPlayer == 2:
            x = int(input("Enter row to insert 2: "))
            y = int(input("Enter column to insert 2: "))
            if board[x][y] == 1 or board[x][y] == 2:
                print("Invalid location. Already filled. Enter location again:")
            else:
                print("Should break")
                board[x][y] = 2
                currentPlayer = 1
                emptySpaces -= 1
        printBoard()
        over = checkWinner()
        if over != None:
            print("Human Wins!")
            break
        if emptySpaces==0:
            print("Game Tied!")
            break

if __name__ == "__main__":
    main()
