from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    if a == b:
        return ""

    visited = [False] * 10000
    parent = [None] * 10000
    command = [''] * 10000

    queue = deque([a])
    visited[a] = True

    while queue:
        curr = queue.popleft()

        next_val = (curr * 2) % 10000
        if not visited[next_val]:
            visited[next_val] = True
            parent[next_val] = curr
            command[next_val] = 'D'
            if next_val == b:
                result = []
                node = b
                while parent[node] is not None:
                    result.append(command[node])
                    node = parent[node]
                return ''.join(reversed(result))
            queue.append(next_val)

        next_val = 9999 if curr == 0 else curr - 1
        if not visited[next_val]:
            visited[next_val] = True
            parent[next_val] = curr
            command[next_val] = 'S'
            if next_val == b:
                result = []
                node = b
                while parent[node] is not None:
                    result.append(command[node])
                    node = parent[node]
                return ''.join(reversed(result))
            queue.append(next_val)

        next_val = (curr % 1000) * 10 + curr // 1000
        if not visited[next_val]:
            visited[next_val] = True
            parent[next_val] = curr
            command[next_val] = 'L'
            if next_val == b:
                result = []
                node = b
                while parent[node] is not None:
                    result.append(command[node])
                    node = parent[node]
                return ''.join(reversed(result))
            queue.append(next_val)

        next_val = (curr % 10) * 1000 + curr // 10
        if not visited[next_val]:
            visited[next_val] = True
            parent[next_val] = curr
            command[next_val] = 'R'
            if next_val == b:
                result = []
                node = b
                while parent[node] is not None:
                    result.append(command[node])
                    node = parent[node]
                return ''.join(reversed(result))
            queue.append(next_val)

    return ""

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
