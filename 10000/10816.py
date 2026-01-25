import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

count = Counter(arr)
print(*[count[t] for t in targets])
