t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    num = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        dist1 = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2
        dist2 = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2
        if dist1 != dist2:
            num += 1
    print(num)