total = 0
mush = 0

for _ in range(10):
    x = int(input())
    total += x
    if abs(100 - total) <= abs(100 - mush):
        mush = total

print(mush)