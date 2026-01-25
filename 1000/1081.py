import sys
input = sys.stdin.readline

def f(n):
    c = [0]*10
    if n < 0: return c
    k = 1
    while k <= n:
        h, m, l = n // (k*10), (n // k) % 10, n % k
        for d in range(10): c[d] += h * k
        for d in range(m): c[d] += k
        c[m] += l + 1
        c[0] -= k
        k *= 10
    return c

L, U = map(int, input().split())
A, B = f(U), f(L-1)
print(sum(i * (A[i] - B[i]) for i in range(10)))