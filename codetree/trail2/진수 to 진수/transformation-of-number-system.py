a, b = map(int, input().split())
n = input()
#A->10진수로 바꾸는 것

sum=0
for i in range(len(n)):
    sum+=int(n[i])*a**(len(n)-1-i)
# print(sum)
#10->B진수로 바꾸는 것
result=[]
while sum>=b:
    result.append(sum%b)
    sum=sum//b
result.append(sum)
result=result[::-1]
print("".join(map(str,result)))

# Please write your code here.