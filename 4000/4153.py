while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    x, y, z = sorted([a, b, c])
    if x*x + y*y == z*z:
        print("right")
    else:
        print("wrong")
