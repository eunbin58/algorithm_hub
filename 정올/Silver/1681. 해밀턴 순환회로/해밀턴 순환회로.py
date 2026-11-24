#완탐으로 풀어야함
import sys
N=int(input())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))
# print(board)

visited=[False]*N
count=0



mins=sys.maxsize
def dfs(depth, sumcount,cur):
    global mins 
    if(sumcount>mins) or (depth!=0 and depth!=N and cur==0 ):
        return
    if(depth==N and cur==0):
        mins=sumcount

    for j in range(len(board[0])):
        if(visited[j]==True or board[cur][j]==0):
            continue
        visited[j]=True
        dfs(depth+1,sumcount+board[cur][j],j)
        #재귀 호출
        visited[j]=False
        #왔던곳 자리 false
    

dfs(0,0,0)
print(mins)