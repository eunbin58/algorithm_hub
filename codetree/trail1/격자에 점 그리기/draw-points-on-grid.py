n,m=map(int,(input().split()))
board=[[0]*n for _ in range(n)]

for i in range(1,m+1):
    x,y=map(int,(input().split()))
    board[x-1][y-1]=i

for i in board:
    print(*i)