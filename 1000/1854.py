import heapq
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

dist = [[float('inf')] * k for _ in range(n + 1)]
pq = [(0, 1)]
dist[1][0] = 0

while pq:
    d, curr = heapq.heappop(pq)

    if d > dist[curr][k-1]:
        continue

    for next_node, weight in adj[curr]:
        new_dist = d + weight
        if new_dist < dist[next_node][k-1]:
            dist[next_node][k-1] = new_dist
            dist[next_node].sort()
            heapq.heappush(pq, (new_dist, next_node))

for i in range(1, n + 1):
    if dist[i][k-1] == float('inf'):
        print(-1)
    else:
        print(dist[i][k-1])
