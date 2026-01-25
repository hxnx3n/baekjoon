import sys
import heapq

input = sys.stdin.readline
INF = 10**18

N = int(input())
water = list(map(int, input().split()))
M = int(input())

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

S, T = map(int, input().split())
S -= 1
T -= 1

dist = [INF]*N
max_water = [0]*N
dist[S] = 0
max_water[S] = water[S]

pq = []
heapq.heappush(pq, (0, -water[S], S))

while pq:
    d, neg_w, u = heapq.heappop(pq)
    w = -neg_w
    if d > dist[u]:
        continue
    if d == dist[u] and w < max_water[u]:
        continue
    for v, cost in graph[u]:
        nd = d + cost
        nw = w + water[v]
        if nd < dist[v]:
            dist[v] = nd
            max_water[v] = nw
            heapq.heappush(pq, (nd, -nw, v))
        elif nd == dist[v] and nw > max_water[v]:
            max_water[v] = nw
            heapq.heappush(pq, (nd, -nw, v))

if dist[T] == INF:
    print(-1)
else:
    print(dist[T], max_water[T])
