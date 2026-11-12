from itertools import combinations
T=int(input())

for tc in range(1,T+1):
    n=int(input())
    data=list(map(int,input().split()))
    max=-1

    combin=list(combinations(data,2))
    # print(combin)
    for i,j in combin:
        flag=True
        result=str(i*j)
        for k in range(len(result)-1):
            if(int(result[k])>int(result[k+1])):
                flag=False
                break
        if(flag==True and max<int(result)):
            max=int(result)
    print(f"#{tc}",max)