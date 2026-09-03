N, B = map(int, input().split())
result=[]
while N>=B:
    result.append(str(N%B))
    N=(N//B)
result.append(str(N))
result=result[::-1]
print("".join(result))
# Please write your code here.