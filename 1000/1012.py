import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    def dfs(y, x):
        field[y][x] = 0
        for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and field[ny][nx]:
                dfs(ny, nx)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)
