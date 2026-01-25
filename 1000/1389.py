import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0
    while queue:
        v = queue.popleft()
        for adj in graph[v]:
            if visited[adj] == -1:
                visited[adj] = visited[v] + 1
                queue.append(adj)
    return sum(visited[1:])

min_sum = float('inf')
person = 0
for i in range(1, n + 1):
    s = bfs(i)
    if s < min_sum:
        min_sum = s
        person = i

print(person)
