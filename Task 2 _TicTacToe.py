import math

board = [' ']*9

def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def check_winner(b, player):
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,6],[2,5,8],[0,4,8],[2,4,6]]
    for x in win:
        if b[x[0]]==b[x[1]]==b[x[2]]==player:
            return True
    return False

def minimax(b, depth, isMax):
    if check_winner(b,'O'): return 10-depth
    if check_winner(b,'X'): return depth-10
    if ' not in b: return 0

    if isMax:
        best=-1000
        for i in range(9):
            if b[i]==' ':
                b[i]='O'
                best=max(best, minimax(b, depth+1, False))
                b[i]=' '
        return best
    else:
        best=1000
        for i in range(9):
            if b[i]==' ':
                b[i]='X'
                best=min(best, minimax(b, depth+1, True))
                b[i]=' '
        return best

def best_move():
    bestVal=-1000; move=-1
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            val=minimax(board,0,False)
            board[i]=' '
            if val>bestVal: bestVal=val; move=i
    return move

print("TIC-TAC-TOE AI - You=X, AI=O")
while True:
    print_board()
    move=int(input("Enter position 0-8: "))
    board[move]='X'
    if check_winner(board,'X'): print_board(); print("You Win!"); break
    ai=best_move(); board[ai]='O'
    if check_winner(board,'O'): print_board(); print("AI Wins!"); break
