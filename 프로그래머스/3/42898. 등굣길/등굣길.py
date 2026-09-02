def solution(m, n, puddles):
    list=[[0]*m for _ in range(n)]
    for pud in puddles:
        list[pud[1]-1][pud[0]-1]=-1
    countlist=[[0]*m for _ in range(n)]
    countlist[0][0]=1
    # print(countlist)
    for i in range(n):
        for j in range(m):
            a=0
            b=0
            if(list[i][j]==-1):
                continue
            if j > 0:
                countlist[i][j] += countlist[i][j-1]%1000000007
            if i > 0:
                countlist[i][j] += countlist[i-1][j] %1000000007
            countlist[i][j]=countlist[i][j]%1000000007
            
            
    # print(list)
    # print(countlist)
    answer = countlist[n-1][m-1]
    return answer