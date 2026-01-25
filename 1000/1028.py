import sys
input = sys.stdin.readline

R, C = map(int, input().split())
mine = [list(map(int, input().strip())) for _ in range(R)]

dir = [[[0]*C for _ in range(R)] for _ in range(4)]

def check(y, x):
    return 0 <= y < R and 0 <= x < C

for i in range(R):
    for j in range(C):
        if mine[i][j]:
            dir[0][i][j] = (dir[0][i-1][j+1] + 1) if check(i-1, j+1) else 1
            dir[1][i][j] = (dir[1][i-1][j-1] + 1) if check(i-1, j-1) else 1

for i in range(R-1, -1, -1):
    for j in range(C-1, -1, -1):
        if mine[i][j]:
            dir[2][i][j] = (dir[2][i+1][j+1] + 1) if check(i+1, j+1) else 1
            dir[3][i][j] = (dir[3][i+1][j-1] + 1) if check(i+1, j-1) else 1

ret = 0
for i in range(R):
    for j in range(C):
        temp = min(dir[0][i][j], dir[2][i][j])
        if ret >= temp:
            continue
        k = j + (temp * 2) - 2
        while k >= j:
            if not check(i, k):
                temp -= 1
            elif dir[1][i][k] >= temp and dir[3][i][k] >= temp:
                ret = max(ret, temp)
                break
            else:
                temp -= 1
            k -= 2

print(ret)
