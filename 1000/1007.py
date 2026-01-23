import sys

input = sys.stdin.readline

T = int(input())


def solve(points, N):
    ans = float("inf")

    def dfs(idx, cnt, sx, sy):
        nonlocal ans
        if cnt > N // 2:
            return
        if idx == N:
            if cnt == N // 2:
                v = sx * sx + sy * sy
                if v < ans:
                    ans = v
            return

        dfs(idx + 1, cnt + 1, sx + points[idx][0], sy + points[idx][1])
        dfs(idx + 1, cnt, sx - points[idx][0], sy - points[idx][1])

    dfs(0, 0, 0, 0)
    return ans**0.5


for _ in range(T):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    print(f"{solve(points, N):.6f}")
