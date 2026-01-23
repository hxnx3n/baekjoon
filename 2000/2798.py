from itertools import combinations
N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
for a, b, c in combinations(cards, 3):
    s = a + b + c
    if s <= M:
        ans = max(ans, s)
print(ans)
