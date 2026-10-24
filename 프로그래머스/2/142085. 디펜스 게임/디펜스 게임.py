#1시간

# def solution(n, k, enemy):
#     answer = 0
#     list=[]
#     sum=0
    
#     # for i in enemy:
#     while k>-1:
#         if(answer==len(enemy)):
#             break
#         i=enemy[answer]
#         #누적합이 n보다 작을때 => 더 더할 수 있음
#         if n>=sum:
#             sum+=i
#             answer+=1
#             list.append(i)
#         #누적합이 n보다 클을때 => 무적권을 사용해야함
#         else:
#             if(k==0):
#                 if(answer>0):
#                     answer-=1
#                 break
#             list.sort()
#             a=list.pop()
#             sum-=a
#             k-=1
#     return answer
import heapq
def solution(n, k, enemy):
    answer = 0
    heap=[]
    sum=0
    
    # for i in enemy:
    while k>-1:
        if(answer==len(enemy)):
            if(n<sum and k<1):
                answer-=1
            break
        i=enemy[answer]
        #누적합이 n보다 작을때 => 더 더할 수 있음
        if n>=sum:
            sum+=i
            answer+=1
            heapq.heappush(heap,-i)
        #누적합이 n보다 클을때 => 무적권을 사용해야함
        else:
            if(k==0):
                if(answer>0):
                    answer-=1
                    print("answer",answer)
                break
            # list.sort()
            a=-heapq.heappop(heap)
            sum-=a
            k-=1
        # print(sum)
        # print(k)
        # print(answer)
    return answer