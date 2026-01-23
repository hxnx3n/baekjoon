import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 10
add = 0
i = 1

while N != 0:
    curr = N % 10
    N //= 10

    cnt[0] -= i

    for j in range(curr):
        cnt[j] += (N + 1) * i

    cnt[curr] += N * i + 1 + add

    for j in range(curr + 1, 10):
        cnt[j] += N * i

    add += curr * i
    i *= 10

print(*cnt)
