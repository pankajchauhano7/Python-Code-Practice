str=["swiss","abcabcd","abcd"]
non_repchar=[]
for s in str:
    char_count={}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c,freq in char_count.items():
           if freq == 1:
                non_repchar.append(c)
print(non_repchar)