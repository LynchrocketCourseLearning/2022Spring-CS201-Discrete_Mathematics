import math
from queue import PriorityQueue

V, E = 6, 8
visited, distance = [False for _ in range(V)], [1000 for _ in range(V)]
graph = [[math.inf for _ in range(V)] for _ in range(V)]
def dijkstra(s):
    distance[s] = 0
    q = PriorityQueue(V)
    q.put_nowait(s)
    while q.qsize()!=0:
        v = q.get_nowait()
        visited[v] = True
        for u in range(V):
            if graph[v][u] == math.inf or visited[u]:
                continue
            else:
                q.put_nowait(u)
            if distance[u] > distance[v] + graph[v][u]:
                distance[u] = distance[v] + graph[v][u]

for _ in range(E):
    v, u, w = list(map(int, input().split()))
    graph[v][u] = w
s = int(input('Please input the source vertex: '))
dijkstra(s)
print(distance)
print(graph)

# # 有/无向图最短路径
# 1 2 2
# 1 3 5
# 3 2 3
# 3 5 2
# 3 4 3
# 2 4 1
# 4 5 4
# 5 1 5
