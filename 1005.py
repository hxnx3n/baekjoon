import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    W = int(input())

    dp = [0] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            dp[i] = time[i]
            q.append(i)

    while q:
        node = q.popleft()
        
        for nxt in graph[node]:
            dp[nxt] = max(dp[nxt], dp[node] + time[nxt])
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                q.append(nxt)

    print(dp[W])