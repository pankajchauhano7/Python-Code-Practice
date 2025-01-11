# Count occurence of character in string
str="My name is Python Programming"
strLow=str.lower()
target='m'
count=0
for c in strLow:
    if c == target:
        count +=1
print(count)
