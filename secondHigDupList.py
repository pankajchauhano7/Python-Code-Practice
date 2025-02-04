#Find Second highest number from duplicate values list
arr = [23, 45, 1, 5, 70, 45, 12, 70, 1, 33, 45]
arr = list(set(arr))  # Remove duplicates
arr.sort(reverse=True)  # Sort in descending order
second_highest = arr[1]  # Second element in sorted array
print(second_highest)