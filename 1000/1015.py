import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

idx = sorted(range(N), key=lambda i: (A[i], i))
P = [0] * N

for i, v in enumerate(idx):
    P[v] = i

print(*P)
