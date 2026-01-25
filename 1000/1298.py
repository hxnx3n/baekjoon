import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

match = [-1] * (N + 1)

def dfs(u, visited):
    for v in adj[u]:
        if visited[v]:
            continue
        visited[v] = True
        if match[v] == -1 or dfs(match[v], visited):
            match[v] = u
            return True
    return False

result = 0
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    if dfs(i, visited):
        result += 1

print(result)
