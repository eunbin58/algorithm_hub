def solution(n):
    answer = []
    #막대기
    rod=[True]+[False]*3
    
    def f(n, s, g):
        if(n==0):
            return 1;
        #선택 안된 막대기가 무엇인지
        rod[s]=True
        rod[g]=True
        middle=0
        for i in range(1,4):
            if(rod[i]==False):
                middle=i
                break;
        rod[s]=False
        rod[g]=False
        # answer.append([s,middle])
        #=> 왜 이걸 없애야 하는지 모르겠어용
        f(n-1,s,middle)
        answer.append([s,g])
        f(n-1,middle,g)
        # answer.append([middle,g])
    
    f(n,1,3)    
    return answer