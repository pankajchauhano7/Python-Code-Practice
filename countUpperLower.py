def UpperLowerCaseCount(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    return upper_count, lower_count
# Example usage
input_string = "Hello World!"
upper, lower = UpperLowerCaseCount(input_string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")