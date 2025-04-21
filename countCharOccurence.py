#count character ocurrence
new_str = "geeksforgeeks"
char_count={}
for char in new_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
print(char_count)
