n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]
rank = []

for i in range(n):
    r = 1
    for j in range(n):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            r += 1
    rank.append(r)

print(*rank)
