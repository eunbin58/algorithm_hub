#숫자가 100,000 => 완전 탐색 불가
#sort해서 뒤부터 비교하는건? 승점 return이니까 최대로 많이 이길 수 있으면 되는거잖아.
#반례가 있을 것 같은데
#A:1,5,10,15 B:1,2,6,14
#그럼 맨 뒤가 b가 더작으면 b에서 작은걸 보내는 방향으로 하면 최대한 점수를 많이 받을 수 있지 않을까?
#근데 그럼 맨 앞쪽에서 다 b가 먹을 수 있는데 못먹게 될 수도 있을 것 같다
#=> 그럼 뒤에껄로 막으면 되서 괜찮다
#결국 풀이법이 생각안나서 ai의 힘들 빌림
from collections import deque
def solution(A, B):
    A.sort()
    B.sort()
    qa=deque(A)
    qb=deque(B)
    answer=0

    for _ in range(len(A)):
        if(qb[-1]>qa[-1]):
            qa.pop()
            qb.pop()
            answer+=1
        else:
            # if(qb[-1]>qa[0]):
            #     answer+=1
            qb.popleft()
            qa.pop()
        # print(qa,qb)
            
    
    return answer