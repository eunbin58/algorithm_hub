n = int(input())
profit = [0]+list(map(int, input().split()))
# max=[0]*(n+1)
# Please write your code here.
#해당까지 최대

for i in range(1,n+1):
    # max[i]=profit[i]
    for j in range(1,i//2+1):
        value=profit[j]+profit[i-j]
        if(value>profit[i]):
            profit[i]=value
print(profit[n])


        

