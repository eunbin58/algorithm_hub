binary = input()
result=0
for i in range(len(binary)):
    result+=int(binary[i])*(2**(len(binary)-1-i))
    
print(result)
# Please write your code here.