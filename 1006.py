import sys

input = sys.stdin.readline

def solve():
    def recur(start, a, b, c):
        for i in range(start, N):
            a[i+1] = min(b[i] + 1, c[i] + 1)
            if up[i] + down[i] <= W:
                a[i+1] = min(a[i+1], a[i] + 1)
            if i > 0 and up[i-1] + up[i] <= W and down[i-1] + down[i] <= W:
                a[i+1] = min(a[i+1], a[i-1] + 2)

            if i < N - 1:
                b[i+1] = a[i+1] + 1
                if up[i] + up[i+1] <= W:
                    b[i+1] = min(b[i+1], c[i] + 1)

                c[i+1] = a[i+1] + 1
                if down[i] + down[i+1] <= W:
                    c[i+1] = min(c[i+1], b[i] + 1)
        return a, b, c

    line = input().split()
    if not line: return
    N, W = map(int, line)
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))

    if N == 1:
        print(1 if up[0] + down[0] <= W else 2)
        return

    a = [0] * (N + 1)
    b = [0] * (N + 1)
    c = [0] * (N + 1)
    b[0], c[0] = 1, 1
    a, b, c = recur(0, a, b, c)
    res = a[N]
    
    if up[0] + up[N-1] <= W:
        a_w = [0] * (N + 1)
        b_w = [0] * (N + 1)
        c_w = [0] * (N + 1)
        a_w[1] = 1
        b_w[1] = 2
        c_w[1] = 1 if down[0] + down[1] <= W else 2
        a_w, b_w, c_w = recur(1, a_w, b_w, c_w)
        res = min(res, c_w[N-1] + 1)

    if down[0] + down[N-1] <= W:
        a_d = [0] * (N + 1)
        b_d = [0] * (N + 1)
        c_d = [0] * (N + 1)
        a_d[1] = 1
        c_d[1] = 2
        b_d[1] = 1 if up[0] + up[1] <= W else 2
        a_d, b_d, c_d = recur(1, a_d, b_d, c_d)
        res = min(res, b_d[N-1] + 1)

    if up[0] + up[N-1] <= W and down[0] + down[N-1] <= W:
        a_b = [0] * (N + 1)
        b_b = [0] * (N + 1)
        c_b = [0] * (N + 1)
        a_b[1] = 0
        b_b[1] = 1
        c_b[1] = 1
        a_b, b_b, c_b = recur(1, a_b, b_b, c_b)
        res = min(res, a_b[N-1] + 2)

    print(res)

T_str = input().strip()
if T_str:
    T = int(T_str)
    for _ in range(T):
        solve()