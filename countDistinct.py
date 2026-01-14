# Given an integer array, this function returns the count of distinct elements in the array.
def count_distinct(arr):
    distinct = []

    for i in arr:
        found = False
        for j in distinct:
            if i == j:
                found = True
                break
        if not found:
            distinct.append(i)

    return len(distinct)

# Example usage:
arr=[1, 2, 2, 3, 4, 4, 5]
print(count_distinct(arr))  # Output: 5