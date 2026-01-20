def solve(x1, y1, r1, x2, y2, r2):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if distance == 0 and r1 == r2:
        return -1
    elif distance == r1 + r2 or distance == abs(r1 - r2):
        return 1
    elif distance > r1 + r2 or distance < abs(r1 - r2):
        return 0
    else:
        return 2


t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(solve(x1, y1, r1, x2, y2, r2))
