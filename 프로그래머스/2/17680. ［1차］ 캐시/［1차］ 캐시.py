#50분걸림
#테케 찾는거 도움받음... 다시 풀어햠...
#중간에서 빠지는 경우도 생각해야함
from collections import deque
def solution(cacheSize, cities):
    #모두 대문자로 변경
    for i in range(len(cities)):
        cities[i]=cities[i].upper()
    answer = 0
    q=deque()
    
    for cur in cities:
        #캐시가 다 찼을 때
        if(len(q)==cacheSize):
            #캐시 안에 있을 때
            curt=-1
            for i in range(len(q)):
                if cur == q[i]:
                    curt=i
                    break
            if curt>-1:
                answer+=1       
                q.append(cur)
                del q[curt]
            #캐시 안에 없을 때
            else:
                answer+=5
                q.append(cur)
                q.popleft()
        #캐시 자리가 남았을때
        else:
            #캐시 안에 있을때
            curt=-1
            for i in range(len(q)):
                if cur == q[i]:
                    curt=i
                    break
            if curt>-1:
                answer+=1       
                q.append(cur)
                del q[curt]
            #캐시 안에 없을 때
            else:
                answer+=5
                q.append(cur)
    return answer