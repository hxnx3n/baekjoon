import sys
import math

input = sys.stdin.readline

n = int(input())

def is_square(x):
    s = int(math.isqrt(x))
    return s*s == x

if is_square(n):
    print(1)
    exit()

for i in range(1, int(math.isqrt(n)) + 1):
    if is_square(n - i*i):
        print(2)
        exit()

tmp = n
while tmp % 4 == 0:
    tmp //= 4
if tmp % 8 == 7:
    print(4)
else:
    print(3)
