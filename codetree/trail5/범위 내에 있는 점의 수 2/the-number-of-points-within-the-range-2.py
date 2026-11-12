n, q = map(int, input().split())
points = list(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]


#pop할꺼라 거꾸로 sort
points.sort(reverse=True)
point1=points[0]
clist=[0]*(point1+1)

count=0

start=points.pop()
#points만큼 돌기
while points:
    cur=points.pop()
    count+=1
    #해당범위에 누적으로 0부터 현재 범위까지 얼마나 있는지 쌓기
    for i in range(start,cur+1):
        clist[i]=count
    start=cur

#points가 1일때와 아닐때 처리
#points의 마지막은 for문을 돌지 않았기 때문에 +1을 따로 처리
if(len(clist)!=1):
    clist[-1]=clist[-2]+1
else:
    clist[0]=1

#예시와 같이 2~3이면 2,3 두개의 점을 가지고 있으므로 count는 clist[3]-clist[1]을 해야함
for a,b in ranges:
    #a가 리스트보다 클때 => 무조건 a와 b는 점이 없으니까 0출력
    if(a>point1):
        print(0)
    #b가 리스트보다 클때 => b를 리스트의 마지막 값으로 변환후 출력
    elif(b>point1):
        if(a==0):
            print(clist[point1])
        else:
            print(clist[point1]-clist[a-1])
    #그 외 나머지
    else:
        if(a==0):
            print(clist[b])
        else:
            print(clist[b]-clist[a-1])