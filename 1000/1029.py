import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

artist_num = int(input())
price_board = [list(map(int, input().strip())) for _ in range(artist_num)]

dp = [[[-1]*10 for _ in range(artist_num)] for __ in range(1 << artist_num)]

def resell(visited, artist, price):
    if dp[visited][artist][price] != -1:
        return dp[visited][artist][price]

    ret = 0
    for i in range(1, artist_num):
        if not (visited & (1 << i)) and price_board[artist][i] >= price:
            ret = max(
                ret,
                resell(visited | (1 << i), i, price_board[artist][i]) + 1
            )

    dp[visited][artist][price] = ret
    return ret

print(resell(1, 0, 0) + 1)
