str="Welcome to python programming"
strLow=str.lower()
count=0
for c in strLow:
    if c != ' ':
        count += 1
print(count)