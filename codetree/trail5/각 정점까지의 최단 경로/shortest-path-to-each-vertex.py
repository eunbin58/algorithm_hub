n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

#1. set으로 priorityQueue =>heap사용
# heap에 넣어서 while heqp이 empty일때 까지
# min_dist가 dist[min_index]와 다르면 최단이 아니기 때문에 continue
# 간선들 보며 최단거리 값 갱신

import heapq
import sys

graph=[[] for _ in range(n+1)]
dist=[sys.maxsize]*(n+1)
# print(dist)
pq=[]

for edge in edges:
    x,y,z=edge
    graph[x].append((y,z))
    graph[y].append((x,z))

dist[k]=0
# print(graph)
heapq.heappush(pq,(0,k))

while pq:
    min_dist, min_index=heapq.heappop(pq)
    # print(min_dist, min_index)

    if min_dist != dist[min_index]:
        continue
    for target_index, target_dist in graph[min_index]:
        newdist=dist[min_index]+target_dist
        if(newdist<dist[target_index]):
            dist[target_index]=newdist
            heapq.heappush(pq,(newdist,target_index))
            # print(newdist)

for j in range(len(dist)):
    if(dist[j]==sys.maxsize):
        dist[j]=-1
# print(dist)
for i in range(1,len(dist)):
    print(dist[i])


        








