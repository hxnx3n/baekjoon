import sys
input = sys.stdin.readline

K = int(input())

n = 2 ** K - 1
sum = n * (n + 1) // 2

print(bin(sum)[2:])
