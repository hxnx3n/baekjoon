import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

left, right = 1, max(lines)
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(line // mid for line in lines)
    if count >= n:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
