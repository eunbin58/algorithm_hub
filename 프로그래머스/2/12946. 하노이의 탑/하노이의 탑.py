def solution(n):
    answer = []
    #원반의 현재 위치 인덱스는 원반 번호
    # disk=[0]*(n+1)
    rod=[True]+[False]*3
    #원반 갯수
    #n
    
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
        f(n-1,s,middle)
        
        answer.append([s,g])
        f(n-1,middle,g)
        # answer.append([middle,g])
    
    f(n,1,3)    
    print(answer)
    return answer