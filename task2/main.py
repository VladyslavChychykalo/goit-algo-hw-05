def binary_search_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)


arr = [1.1, 2.3, 3.5, 4.4, 5.5, 6.7]
target = 4.0

result = binary_search_upper_bound(arr, target)
print(result)
