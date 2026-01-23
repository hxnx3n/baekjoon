import sys

def solve():
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]
    min_seg, max_seg = 2, 7
    
    s = sys.stdin.readline().strip()
    if not s: return
    n = len(s)
    target = sum(segments[int(d)] for d in s)
    def find(idx, current_sum, is_greater, current_num_str):
        remaining = n - idx
        if not (current_sum + remaining * min_seg <= target <= current_sum + remaining * max_seg):
            return None
        
        if idx == n:
            return current_num_str if current_sum == target else None

        start_digit = int(s[idx]) if not is_greater else 0
        for d in range(start_digit, 10):
            res = find(idx + 1, current_sum + segments[d], is_greater or (d > start_digit), current_num_str + str(d))
            if res is not None:
                return res
        return None

    current_val = int(s)
    limit = 10**n
    found_res = None

    for i in range(n - 1, -1, -1):
        prefix = s[:i]
        prefix_sum = sum(segments[int(d)] for d in prefix)
        for d in range(int(s[i]) + 1, 10):
            res = find(i + 1, prefix_sum + segments[d], True, prefix + str(d))
            if res:
                found_res = int(res) - current_val
                break
        if found_res is not None: break

    if found_res is not None:
        print(found_res)
    else:
        res = find(0, 0, True, "")
        print(limit - current_val + int(res))

solve()