import sys
input = sys.stdin.readline

mn, mx = map(int, input().split())
size = mx - mn + 1
check = [True] * size

i = 2
while i * i <= mx:
    sq = i * i
    start = ((mn + sq - 1) // sq) * sq
    for j in range(start, mx + 1, sq):
        check[j - mn] = False
    i += 1

print(sum(check))
