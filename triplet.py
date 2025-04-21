arr=[12,3,4,1,6,9]
tar=24

def three_sum(arr,tar):
    arr.sort()
    result=[]
    
    for i in range(len(arr)-2):
        if i>0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1
    
        while left<right:
            cur_sum = arr[i]+arr[left]+arr[right]
        
            if tar == cur_sum:
                result.append((arr[i],arr[left],arr[right]))
                left += 1
                right -= 1
            
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right += 1
        
            elif cur_sum < tar:
                left += 1
        
            else:
                right -= 1
            
    return result
    
print(three_sum(arr,tar))
            
        