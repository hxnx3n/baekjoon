N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

sum_score = 0
for s in size:
    sum_score += (s + T - 1) // T

print(sum_score)
print(N // P, N % P)
