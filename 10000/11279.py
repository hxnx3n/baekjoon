import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        print(-heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, -x)
