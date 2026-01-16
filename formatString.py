#Patterned String Formatter
s="banana"

def format_string(s):
    result=""
    i=0
    
    for ch in s:
        count=0
        while count<= i:
            result = result+ch
            count = count+1
        if i < len(s)-1:
            result = result+"+"
        i=i+1
    return result
print(format_string(s))
        