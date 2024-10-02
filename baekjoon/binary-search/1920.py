# 1. binary search 직접 구현
def binary_search(arr, target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for arr in arr2:
    if binary_search(arr1, arr):
        print(1)
    else:
        print(0)

# 2. 모듈 사용
import bisect

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for arr in arr2:
    idx = bisect.bisect_left(arr1, arr)
    
    if idx < n and arr1[idx] == arr:
        print(1)
    else:
        print(0)

# 3. set 사용
n = int(input())
arr1 = set(map(int, input().split()))
m = int(input())
arr2 = set(map(int, input().split()))

for i in arr2:
    print(1) if i in arr1 else print(0)