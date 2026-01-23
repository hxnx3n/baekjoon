import sys
input = sys.stdin.readline

N = int(input())
sum = []

for i in range(N + 1):
    sum.append(bin(i)[2:])

print("".join(sum))