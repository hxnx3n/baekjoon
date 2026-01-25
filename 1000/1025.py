import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
A = [input().strip() for _ in range(N)]

ans = -1

for i in range(N):
    for j in range(M):
        for di in range(-N, N + 1):
            for dj in range(-M, M + 1):
                if di == 0 and dj == 0:
                    continue
                x, y = i, j
                num = ""
                while 0 <= x < N and 0 <= y < M:
                    num += A[x][y]
                    v = int(num)
                    r = int(math.isqrt(v))
                    if r * r == v:
                        ans = max(ans, v)
                    x += di
                    y += dj

print(ans)
