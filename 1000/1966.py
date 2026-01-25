from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque([(i, int(x)) for i, x in enumerate(input().split())])
    count = 0
    while q:
        idx, val = q.popleft()
        if any(val < other for _, other in q):
            q.append((idx, val))
        else:
            count += 1
            if idx == m:
                print(count)
                break
