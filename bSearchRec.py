
def bSearchRec(arr,left,right,target):
    if left>right:
        return -1
    
    mid= left+(right-left)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bSearchRec(arr,left,mid-1,target)
    else:
        return bSearchRec(arr, mid+1, right,target)

arr = [1,2,3,4,5,6,7]
target = 7
left=0
right=len(arr)-1

print(bSearchRec(arr,left,right,target))