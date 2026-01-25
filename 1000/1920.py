n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

arr.sort()

def binary_search(array, x):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return 1
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for t in target:
    print(binary_search(arr, t))
