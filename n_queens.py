n = 6
board = [["  ." for i in range(n)] for j in range(n)]
def is_safe(n,row,col):
    # coloumn 
    for i in range(n):
        if board[i][col] == "  Q":
            return False
    # left diagonal
    i , j = row-1,col-1
    while i>=0 and j>=0 :
        if board[i][j] == "  Q":
            return False 
        i-=1
        j-=1
    # right diagonal
    i , j = row-1,col+1
    while i >= 0 and j <= n-1 :
        if board[i][j] == "  Q":
            return False
        i-=1
        j+=1
    return True
def solve(row):
    if row == n:
        for i in board:
            print(*i)
        print()
        return
    for col in range(n):
        if is_safe(n,row,col):
            board[row][col] = "  Q"
            solve(row+1)
            board[row][col] = "  ."
solve(0)