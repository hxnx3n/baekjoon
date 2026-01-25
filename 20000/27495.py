import sys
input = sys.stdin.readline

matrix = [input().split() for _ in range(9)]

v = []
for i in range(1, 9, 3):
    for j in range(1, 9, 3):
        if i == 4 and j == 4:
            continue
        v.append((matrix[i][j], i, j))

v.sort(key=lambda x: x[0])

for idx, (center, r, c) in enumerate(v, 1):
    print(f"#{idx}. {center}")
    temp = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            temp.append(matrix[r + dr][c + dc])
    temp.sort()
    for i, val in enumerate(temp, 1):
        print(f"#{idx}-{i}. {val}")
