isbn = input().strip()
result = 0
star_index = isbn.index('*') if '*' in isbn else -1

for i in range(13):
    if isbn[i] != '*':
        result += int(isbn[i]) * (1 if i % 2 == 0 else 3)

if star_index % 2 == 0:
    print((10 - result % 10) % 10)
else:
    for i in range(10):
        if (result + i * 3) % 10 == 0:
            print(i)
            break
