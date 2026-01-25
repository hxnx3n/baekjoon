nums = list(map(int, input().split()))
print(sum(x * x for x in nums) % 10)
