import sys
import re
input = sys.stdin.readline

p = re.compile(r'^(100+1+|01)+$')

T = int(input())
for _ in range(T):
    s = input().strip()
    print("YES" if p.match(s) else "NO")
