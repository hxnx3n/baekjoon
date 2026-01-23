import sys

for line in sys.stdin:
    n, k = map(int, line.split())
    result = n
    coupon = n

    while coupon >= k:
        new = coupon // k
        result += new
        coupon = coupon % k + new

    print(result)
