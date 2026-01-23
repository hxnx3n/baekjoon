r1, c1, r2, c2 = map(int, input().split())
def val(i, j):
    m = max(abs(i), abs(j))
    base = (2*m+1)**2
    if i == m and j != -m:
        return base - (m - j)
    base -= 2*m
    if j == -m and i != -m:
        return base - (m - i)
    base -= 2*m
    if i == -m and j != m:
        return base - (j + m)
    base -= 2*m
    return base - (i + m)
nums = [[val(i, j) for j in range(c1, c2+1)] for i in range(r1, r2+1)]
maxlen = max(len(str(x)) for row in nums for x in row)
for row in nums:
    print(" ".join(str(x).rjust(maxlen) for x in row))
