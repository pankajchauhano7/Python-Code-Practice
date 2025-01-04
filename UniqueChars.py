from collections import Counter
str=['swiss','abcabcd','abcd']
char_count=Counter(" ".join(str))
non_repchar=[char for char,count in char_count.items() if count == 1]
print(non_repchar)