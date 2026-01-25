import sys
input = sys.stdin.readline

s, N, K, R1, R2, C1, C2 = map(int, input().split())

def is_black(x, y):
    while s > 0:
        size = N ** s
        block = size // N
        cx = (x % size) // block
        cy = (y % size) // block
        if (N - K) // 2 <= cx < (N + K) // 2 and (N - K) // 2 <= cy < (N + K) // 2:
            return 1
        x %= block
        y %= block
        s -= 1
    return 0

for i in range(R1, R2 + 1):
    row = []
    for j in range(C1, C2 + 1):
        x, y = i, j
        ss = s
        black = 0
        while ss > 0:
            size = N ** ss
            block = size // N
            cx = (x % size) // block
            cy = (y % size) // block
            if (N - K) // 2 <= cx < (N + K) // 2 and (N - K) // 2 <= cy < (N + K) // 2:
                black = 1
                break
            x %= block
            y %= block
            ss -= 1
        row.append('1' if black else '0')
    print(''.join(row))
