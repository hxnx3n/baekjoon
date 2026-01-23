def fibonacci(n):
    z = [1, 0]
    o = [0, 1]

    for i in range(2, n + 1):
        z.append(z[i - 1] + z[i - 2])
        o.append(o[i - 1] + o[i - 2])

    return z[n], o[n]

t = int(input())

for _ in range(t):
    n = int(input())
    z, o = fibonacci(n)
    print(z, o)