n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

result=[0]*2000
cur=0
for i in range(n):
    if(dir[i]=="R"):
        for _ in range(x[i]):
            result[cur+1000]+=1
            cur+=1
    else:
        for _ in range(x[i]):
            cur-=1
            result[cur+1000]+=1
            
            
answer=0
for count in result:
    if(count>=2):
        answer+=1
# print(result)
print(answer)
# Please write your code here.