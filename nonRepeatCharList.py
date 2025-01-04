str=["swiss","abcabcd","abcd"]
non_repchar=[]
char_count={}
for s in str:
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
for c,freq in char_count.items():
      if freq == 1:
        non_repchar.append(c)
print(non_repchar)