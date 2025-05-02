def fourth_largest(arr):
    if len(arr) < 4:
        return None  # Not enough elements

    first = second = third = fourth = float('-inf')

    for num in arr:
        if num > first:
            fourth = third
            third = second
            second = first
            first = num
        elif num > second and num != first:
            fourth = third
            third = second
            second = num
        elif num > third and num != second and num != first:
            fourth = third
            third = num
        elif num > fourth and num != third and num != second and num != first:
            fourth = num

    return fourth if fourth != float('-inf') else None

arr = [7, 2, 10, 4, 3, 8, 5]
print(fourth_largest(arr))  # Output: 5

