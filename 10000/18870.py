import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sorted_unique = sorted(set(arr))
compress = {num: i for i, num in enumerate(sorted_unique)}

print(' '.join(str(compress[x]) for x in arr))
