n,m=map(int,(input().split()))
board=[[0]*n for _ in range(n)]

for _ in range(m):
    x,y=map(int,(input().split()))
    board[x-1][y-1]=1

for i in board:
    print(*i)
        

