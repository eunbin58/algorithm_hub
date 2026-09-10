n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

list=[0]*200
for tuple in segments:
    start,end=tuple[0],tuple[1]
    start+=100
    end+=100
    for check in range(start,end):
        list[check]+=1

print(max(list))
# Please write your code here.