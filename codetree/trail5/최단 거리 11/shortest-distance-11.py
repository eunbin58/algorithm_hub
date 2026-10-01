import sys
import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
graph=[[]for _ in range(n+1)]
dist=[sys.maxsize]*(n+1)
path=[[] for _ in range(n+1)]
pq=[]
comparelist=[0]*2
# print(dist)
# print(path)

for edge in edges:
    x,y,z=edge
    graph[x].append((y,z))
    graph[y].append((x,z))

# print(graph)
dist[A]=0
path[A].append(A)

def compare(a,b):
    if(len(a)<len(b)):
        for i in range(len(a)):
            if(a[i]==b[i]):
                continue
            elif(a[i]>b[i]):
                return b
            else:
                return a
    else:
        for i in range(len(b)):
            if(a[i]==b[i]):
                continue
            elif(a[i]>b[i]):
                return b
            else:
                return a
    return a if len(a)<=len(b) else b

heapq.heappush(pq,(0,A))

while pq:
    min_dist, min_index=heapq.heappop(pq)
    # print(path)
    if( min_dist != dist[min_index]):
        continue
    for target_index, target_dist in graph[min_index]:
        newdist=dist[min_index]+target_dist
        if(newdist<=dist[target_index]):
            if(newdist<dist[target_index]):
                dist[target_index]=newdist
                path[target_index]=path[min_index]+[target_index]
            else:
                dist[target_index]=newdist
                path[target_index]=compare(path[target_index],path[min_index]+[target_index])
        
            # dist[target_index]=newdist
            # path[target_index]=compare(str(path[target_index]),str(path[min_index])+str(target_index))
            # print(dist)
            # print(path)
            heapq.heappush(pq,(newdist,target_index))
print(dist[B])
# print(path)
print(*path[B])
# for path in path[B]:
#     print(path,end=" ")