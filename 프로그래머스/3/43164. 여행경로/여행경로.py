#로직은 짰는데 구현을 못하겠어서 dfs 구현하는 부분을 ai에게 힌트를 받았어요...
#dfs 쉬운 문제부터 많이 풀어야 할 것 같습니다
#완전 자승자박
def solution(tickets):
    answer = []
    dic={}
    ticket=0
    #없으면 넣고 있으면 추가하고
    for i in tickets:
        dic.setdefault(i[0],[]).append(i[1])
        ticket+=1
    visit={key:[False] *len(value) for key, value in dic.items()}
    # print(visit)
    
    for key in dic:
        dic[key].sort()
    
    result=["ICN"]
    count=0
    def dfs(cur, count):
        nonlocal answer
        
        #이건 획기적이라 생각해요. 아니 answer에 답이 있으면 바로 return 하는 방법...
        if answer:
            return
        
        #모든 항공권 사용했나요? 그럼 그게 답이에요
        if(count==ticket):
            answer=result[:]
            return 
        #현재 공항에서 어디 갈 수 있나요?
        if cur in dic:
            for i in range(len(dic[cur])):
                #i번째 공항안갔으면?
                if(visit[cur][i]==False):
                    #방문처리
                    visit[cur][i]=True
                    result.append(dic[cur][i])
                    #다음 공항으로 dfs
                    dfs(dic[cur][i],count+1)
                    #방문 복구처리
                    visit[cur][i]=False
                    result.pop()
    dfs("ICN",0)
    # print(answer)
    return answer