from collections import deque
def solution(board):
    answer = 0
    start=(0,0)
    goal=(0,0)
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visit=[[0]*len(board[0]) for _ in range(len(board))]

    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col]=='G'):
                goal=(col,row)
            elif(board[row][col]=='R'):
                start=(col,row)
    
    q=deque()
    q.append((start[0],start[1],0,0,0))
    # q.append((4,0,1,0))
    # q.append((4,1,0,-1))
    # q.append((6,1,-1,0))
    # xlen=len(board[0])
    # ylen=len(board)
    # print(xlen, ylen)
    flag=False
    result=-1
    
    while q:
        x,y,vx,vy,count=q.popleft()
        
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # print(nx,ny,vx,vy,dx[i],dy[i])
            #내가 왔던 방향이면
            
            if(vx==dx[i] and vy==dy[i]):
                continue
            # print(nx,ny,vx,vy,dx[i],dy[i])
            if( nx<0 or ny<0 or nx>=len(board[0]) or ny>=len(board) ):
                continue
            # print(nx,ny,vx,vy,dx[i],dy[i])
            if(board[ny][nx]=='D'):
                continue
            # print(nx,ny,vx,vy,dx[i],dy[i])
            while( nx>=0 and ny>=0 and nx<len(board[0]) and ny<len(board) and board[ny][nx]!='D'):
                nx=nx+dx[i]
                ny=ny+dy[i]
                # if( nx<0 or ny<0 or nx>=len(board[0]) or ny>=len(board)):
                #     continue
            if(nx-dx[i]==start[0] and ny-dy[i]==start[1]):
                continue
            if(nx-dx[i]==goal[0] and ny-dy[i]==goal[1]):
                flag=True
                break
            #온길로는 가지 않게 하기 (d에 부딪힌 위치 x,y, 방금 왔던 방향 x,y)
            # print('p',nx-dx[i],ny-dy[i],dx[i]*-1,dy[i]*-1,count+1)
            
            #debug
            # q.append((4,0,1,0))
            # q.append((6,1,0,-1))
            if(visit[ny-dy[i]][nx-dx[i]]!=0):
                continue
            q.append((nx-dx[i],ny-dy[i],dx[i]*-1,dy[i]*-1,count+1))
            visit[ny-dy[i]][nx-dx[i]]=count+1
        if flag:
            result=count+1
            break  
                    
                    
                    
                    
                    

    
    # print(result)
    answer=result

    
    return answer