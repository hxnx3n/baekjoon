import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [0] * (N + 1)
tree = [0] * (N + 1)

def update(i, diff):
    while i <= N:
        tree[i] += diff
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s

for i in range(1, N + 1):
    arr[i] = int(input())
    update(i, arr[i])

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(b, diff)
    else:
        print(query(c) - query(b - 1))
