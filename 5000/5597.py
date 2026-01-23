sum = [False] * 31

for _ in range(28):
    sum[int(input())] = True

for i in range(1, 31):
    if not sum[i]:
        print(i)
