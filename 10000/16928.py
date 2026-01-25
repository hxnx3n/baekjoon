import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [i for i in range(101)]

for _ in range(n + m):
    x, y = map(int, input().split())
    board[x] = y

visited = [-1] * 101
queue = deque([1])
visited[1] = 0

while queue:
    pos = queue.popleft()
    if pos == 100:
        print(visited[pos])
        break
    for dice in range(1, 7):
        nxt = pos + dice
        if nxt <= 100 and visited[board[nxt]] == -1:
            visited[board[nxt]] = visited[pos] + 1
            queue.append(board[nxt])
