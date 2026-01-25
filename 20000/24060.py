import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
ans = -1

def merge_sort(p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(p, q)
    merge_sort(q + 1, r)
    merge(p, q, r)

def merge(p, q, r):
    global cnt, ans
    tmp = []
    i, j = p, q + 1

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1

    for idx, v in enumerate(tmp):
        A[p + idx] = v
        cnt += 1
        if cnt == K:
            ans = v

merge_sort(0, N - 1)
print(ans)
