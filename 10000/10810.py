N, M = map(int, input().split())
arr = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        arr[x] = k

print(*arr)
