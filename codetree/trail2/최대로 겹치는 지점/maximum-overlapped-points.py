n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
list=[0]*101
for i in range(n):
    for j in range(segments[i][0],segments[i][1]+1):
        list[j]=list[j]+1
print(max(list))
# Please write your code here.