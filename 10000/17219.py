import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pw = dict(input().split() for _ in range(n))

for _ in range(m):
    print(pw[input().strip()])
