import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    sum = pow(a, b, 10)
    print(10 if sum == 0 else sum)