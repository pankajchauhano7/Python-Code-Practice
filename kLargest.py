# Given an array of integers, return the k largest elements in the array.
def k_largest(arr,k):
    n=len(arr)
    result= []
    for _ in range(k):
        max_index=0
        for i in range(1,n):
            if arr[i]>arr[max_index]:
                max_index=i
        result.append(arr[max_index])
        arr[max_index]=-1
    return result

# Example usage:
arr=[3,1,5,12,2,11]
k=2
print(k_largest(arr,k))  # Output: [12, 11]