# Function to find the maximum element and return it along with all subsequent elements

def max_with_subsequents(arr):
    max_val = arr[0]
    max_index = 0

    i = 1
    while i < len(arr):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
        i += 1

    result = []
    j = max_index
    while j < len(arr):
        result.append(arr[j])
        j += 1

    print(result)

# Example
arr = [12, 13, 2, 5, 6, 8, 9]
max_with_subsequents(arr)