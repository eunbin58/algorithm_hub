from itertools import product
def solution(word):
    answer = 0
    diction=[]
    data=["A","E","I","O","U"]
    for i in range(1,6):
        comrep=list(map(''.join,product(data,repeat=i)))
        diction+=comrep
    diction.sort()
    # print(diction)
    print(diction.index(word))
    answer=diction.index(word)+1
    return answer