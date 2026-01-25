from collections import deque

n, k = map(int, input().split())
dq = deque(range(1, n + 1))
result = []

while dq:
    dq.rotate(-(k-1))
    result.append(dq.popleft())

print("<" + ", ".join(map(str, result)) + ">")
