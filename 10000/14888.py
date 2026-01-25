import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_val = -1_000_000_000
min_val = 1_000_000_000

def dfs(idx, cur, add, sub, mul, div):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, cur)
        min_val = min(min_val, cur)
        return
    
    if add:
        dfs(idx+1, cur + nums[idx], add-1, sub, mul, div)
    if sub:
        dfs(idx+1, cur - nums[idx], add, sub-1, mul, div)
    if mul:
        dfs(idx+1, cur * nums[idx], add, sub, mul-1, div)
    if div:
        if cur < 0:
            dfs(idx+1, -(-cur // nums[idx]), add, sub, mul, div-1)
        else:
            dfs(idx+1, cur // nums[idx], add, sub, mul, div-1)

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(max_val)
print(min_val)
