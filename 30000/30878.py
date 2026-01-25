import math

M = int(input())

if M >= 60:
    print("1/1")
else:
    num = 3*M*M*(60-M) + M*M*M
    den = 60*60*60

    g = math.gcd(num, den)
    print(f"{num//g}/{den//g}")
