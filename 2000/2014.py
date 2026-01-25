import sys
import heapq

input = sys.stdin.readline

K, N = map(int, input().split())
primes = list(map(int, input().split()))

heap = []
for p in primes:
    heapq.heappush(heap, p)

ans = 0
for _ in range(N):
    ans = heapq.heappop(heap)
    for p in primes:
        if ans * p > 2**31:
            break
        heapq.heappush(heap, ans * p)
        if ans % p == 0:
            break

print(ans)
