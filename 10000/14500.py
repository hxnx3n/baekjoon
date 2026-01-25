N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

shapes = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)],
        [(0,1), (1,0), (1,1)],
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)],
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)],
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)],
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)],
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)],
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)]]

def calc(i,j,tet) :
    temp = board[i][j]
    for di,dj in tet :
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0<= nj < M :
            temp += board[ni][nj]
        else :
            return 0
    return temp


ans = 0
for i in range (N) :
    for j in range (M) :
        for tet in shapes:
            temp = calc(i,j,tet)
            ans = max(temp, ans)

print(ans)
