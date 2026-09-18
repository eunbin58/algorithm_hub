n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

result=[0]*200002

cur=0
for i in range(n):
    if(dir[i]=="R"):
        for _ in range(x[i]):
            result[cur+100000]="B"
            cur+=1
        cur-=1
    if(dir[i]=="L"):
        for _ in range(x[i]):
            result[cur+100000]="W"
            cur-=1
        cur+=1

white=0
black=0
# print(result)
for cur in result:
    if(cur=="B"):
        black+=1
    elif(cur=="W"):
        white+=1
print(white, black)
            
# Please write your code here.