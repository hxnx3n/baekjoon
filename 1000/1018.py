import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

ans = 64

for i in range(N - 7):
    for j in range(M - 7):
        c1 = c2 = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if board[i + x][j + y] != 'W':
                        c1 += 1
                    if board[i + x][j + y] != 'B':
                        c2 += 1
                else:
                    if board[i + x][j + y] != 'B':
                        c1 += 1
                    if board[i + x][j + y] != 'W':
                        c2 += 1
        ans = min(ans, c1, c2)

print(ans)
