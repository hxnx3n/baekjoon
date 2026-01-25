import math

while True:
    n = int(input().strip())
    if n == 0:
        break
    L = list(map(int, input().split()))
    
    h = [x * math.sqrt(2) for x in L]
    
    c = [0] * n
    
    for i in range(n):
        c[i] = h[i] / 2
        for j in range(i):
            c[i] = max(c[i], c[j] + (h[i] + h[j]) / 2)
    
    visible = []
    for i in range(n):
        ok = True
        for j in range(n):
            if j == i:
                continue
            if h[j] - abs(c[i] - c[j]) >= h[i]:
                ok = False
                break
        if ok:
            visible.append(i+1)
    print(*visible)
    exit()
