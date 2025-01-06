arr=[64, 34, 25, 12, 22, 11, 90] # Bubble Sort

for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)
