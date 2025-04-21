str= "This cakE is tasty. I will bake this CaKe again , for everyone."
new_str = str.upper()
words = new_str.split()
char_count={}
for char in words:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
print(char_count)
