# Find Duplicate in array
arr=[1,2,3,1,2,4]
seen=set()
duplicate=[]
for dup in arr:
    if dup in seen:
        duplicate.append(dup)
    else:
        seen.add(dup)

print("Duplicate in list are : "+str(seen))
        
        