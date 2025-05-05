def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    # Merge elements in order
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged

# Example
a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]
print(merge_sorted_arrays(a, b))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 10]
