import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    seat = [input().strip() for _ in range(N)]

    valid = []
    for i in range(N):
        mask = 0
        for j in range(M):
            if seat[i][j] == '.':
                mask |= 1 << j
        valid.append(mask)

    dp = [{} for _ in range(N)]

    for m in range(1 << M):
        if (m & (m << 1)) == 0 and (m & valid[0]) == m:
            dp[0][m] = bin(m).count('1')

    for i in range(1, N):
        for m in range(1 << M):
            if (m & (m << 1)) or (m & valid[i]) != m:
                continue
            c = bin(m).count('1')
            for pm in dp[i - 1]:
                if (m & (pm << 1)) == 0 and (m & (pm >> 1)) == 0:
                    dp[i][m] = max(dp[i].get(m, 0), dp[i - 1][pm] + c)

    print(max(dp[N - 1].values(), default=0))
