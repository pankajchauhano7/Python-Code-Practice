#Check missing number from list
arr = [1,2,3,5,6,7]
arrLen = len(arr)+1
sum = arrLen*(arrLen+1)//2
actualSum=0
for n in arr:
    actualSum = n+actualSum
missingNum = sum-actualSum
print(f"Missing Number : {missingNum}")