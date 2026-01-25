import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * M
prefix = 0
result = 0

cnt[0] = 1

for x in A:
    prefix = (prefix + x) % M
    result += cnt[prefix]
    cnt[prefix] += 1

print(result)
