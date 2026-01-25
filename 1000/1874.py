import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
curr = 1
possible = True

for _ in range(n):
    num = int(input())
    while curr <= num:
        stack.append(curr)
        result.append('+')
        curr += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print("NO")
