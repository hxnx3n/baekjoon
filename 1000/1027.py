import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))

result = 0

for i1, y1 in enumerate(buildings):
    x1 = i1 + 1

    visible_right = 0
    cur_dy = None
    cur_dx = None
    for i2 in range(i1 + 1, N):
        dy = buildings[i2] - y1
        dx = (i2 + 1) - x1
        if cur_dy is None or cur_dy * dx < dy * cur_dx:
            cur_dy = dy
            cur_dx = dx
            visible_right += 1

    visible_left = 0
    cur_dy = None
    cur_dx = None
    for i3 in range(i1 - 1, -1, -1):
        dy = buildings[i3] - y1
        dx = (i3 + 1) - x1
        if cur_dy is None or cur_dy * dx > dy * cur_dx:
            cur_dy = dy
            cur_dx = dx
            visible_left += 1

    result = max(result, visible_left + visible_right)

print(result)
