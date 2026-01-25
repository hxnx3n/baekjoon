import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

for i in range(n - 1):
    s1 = arr[i]
    s2 = arr[i + 1]

    ok = False
    for j in range(1, m + 1):
        if s1[m - j:] == s2[:j] or s1[:j] == s2[m - j:]:
            ok = True
            break

    if not ok:
        print(0)
        sys.exit(0)

print(1)
