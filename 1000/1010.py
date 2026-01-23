import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    num = min(a, b - a)
    res = 1
    for i in range(1, num + 1):
        res = res * (b - num + i) // i
    print(res)
