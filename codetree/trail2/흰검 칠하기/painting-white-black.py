n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

result=[[0]*3 for _ in range(200002)]

cur=0
for i in range(n):
    if(dir[i]=="R"):
        for _ in range(x[i]):
            if(result[cur+100000][1]>=2 and result[cur+100000][2]>=2):
                result[cur+100000][0]="G"
                cur+=1
            else:
                result[cur+100000][0]="B"
                result[cur+100000][1]+=1
                cur+=1
        cur-=1
    if(dir[i]=="L"):
        for _ in range(x[i]):
            if(result[cur+100000][1]>=2 and result[cur+100000][2]>=2):
                result[cur+100000][0]="G"
                cur-=1
            
            else:
                result[cur+100000][0]="W"
                result[cur+100000][2]+=1
                cur-=1
        cur+=1

answer=[0]*3
# print(result)
for cur in result:
    if(cur[0]=="G" or (cur[1]>=2 and cur[2]>=2) ):
        answer[2]+=1
    elif(cur[0]=="B"):
        answer[1]+=1
    elif(cur[0]=="W"):
        answer[0]+=1
print(*answer)
            
# Please write your code here.