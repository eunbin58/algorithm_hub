n, q = map(int, input().split())
points = list(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]


# Please write your code here.
#pop할꺼라 거꾸로 sort
points.sort(reverse=True)
point1=points[0]
clist=[0]*(point1+1)
start=points.pop()

count=0
# print(points)
while points:
    cur=points.pop()
    count+=1
    for i in range(start,cur+1):
        clist[i]=count
    
    start=cur
if(len(clist)!=1):
    clist[-1]=clist[-2]+1
else:
    clist[0]=1

# print(clist)
for a,b in ranges:
    if(a>point1):
        print(0)
    elif(b>point1):
        if(a==0):
            print(clist[point1])
        # b=point[0]
        else:
            print(clist[point1]-clist[a-1])
    else:
        if(a==0):
            print(clist[b])
        else:
            print(clist[b]-clist[a-1])