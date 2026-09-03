N = input()
n=0
for i in range(len(N)):
    n+=int(N[i])*2**(len(N)-1-i)

n*=17
print(bin(n)[2:])
# Please write your code here.