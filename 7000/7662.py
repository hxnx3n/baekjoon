import sys
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    entry = dict()
    idx = 0

    for _ in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            entry[idx] = True
            idx += 1
        else:  # D
            if num == 1:
                while max_heap and not entry.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)
                if max_heap:
                    entry[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not entry.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)
                if min_heap:
                    entry[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not entry.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    while max_heap and not entry.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
