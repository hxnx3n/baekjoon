N, L = map(int, input().split())
found = False
for length in range(L, 101):
    tmp = N - (length * (length - 1) // 2)
    if tmp < 0:
        continue
    if tmp % length == 0:
        start = tmp // length
        if start >= 0:
            print(*range(start, start + length))
            found = True
            break
if not found:
    print(-1)
