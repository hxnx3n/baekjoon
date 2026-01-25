import sys
input = sys.stdin.readline

N = int(input())
trees = [tuple(map(int, input().split())) for _ in range(N)]

answer = N

for i in range(N):
    for j in range(N):
        x1 = min(trees[i][0], trees[j][0])
        x2 = max(trees[i][0], trees[j][0])

        for k in range(N):
            for l in range(N):
                y1 = min(trees[k][1], trees[l][1])
                y2 = max(trees[k][1], trees[l][1])

                inside = []
                outside = []

                for x, y, length in trees:
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        inside.append((x, y, length))
                    else:
                        outside.append(length)

                perimeter = 2 * ((x2 - x1) + (y2 - y1))

                outside.sort(reverse=True)

                total = 0
                cut = 0
                for l in outside:
                    total += l
                    cut += 1
                    if total >= perimeter:
                        answer = min(answer, cut)
                        break

print(answer)
