import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0

def count_colors(x, y, size):
    global white, blue
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                half = size // 2
                count_colors(x, y, half)
                count_colors(x, y + half, half)
                count_colors(x + half, y, half)
                count_colors(x + half, y + half, half)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

count_colors(0, 0, n)
print(white)
print(blue)
