import sys
from collections import deque

input = sys.stdin.readline


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edges in graph:
    edges.sort()

visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj)

def bfs(start):
    visited_bfs = [False] * (n + 1)
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for adj in graph[node]:
            if not visited_bfs[adj]:
                visited_bfs[adj] = True
                queue.append(adj)

dfs(v)
print()
bfs(v)
