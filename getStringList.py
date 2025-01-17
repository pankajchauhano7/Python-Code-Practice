# Get STring from list
l=[1,2,"Pankaj",4,"Sayan"]
new_l=[]
for item in l:
    if isinstance(item,str):
        new_l.append(item)
print(new_l)