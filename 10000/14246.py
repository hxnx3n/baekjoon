import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = 0
s = 0
left = 0

for right in range(N):
    s += A[right]
    while s > K:
        ans += N - right
        s -= A[left]
        left += 1

print(ans)
