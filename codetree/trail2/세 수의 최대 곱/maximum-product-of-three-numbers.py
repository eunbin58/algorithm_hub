n = int(input())
arr = list(map(int, input().split()))

#음수끼리 곱했을때 (음수가 2개이면 됌
arr.sort()
# print(arr)

if(arr[0]<0 and arr[1]<0):
    if(arr[-1]>0):
        if(arr[0]*arr[1]>arr[-1]*arr[-2]):
            result=arr[0]*arr[1]*arr[-1]
        else:
            result=arr[-1]*arr[-2]*arr[-3]
    else:
        result=arr[-1]*arr[-2]*arr[-3]
else:
    result=arr[-1]*arr[-2]*arr[-3]
# Please write your code here.
print(result)