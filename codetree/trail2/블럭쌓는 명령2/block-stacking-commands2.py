n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
list=[0]*(n+1)

for i in commands:
    start,end=i[0],i[1]
    for j in range(start, end+1):
        # print(j)
        list[j]+=1
print(max(list))
# Please write your code here.
