input_str = "aaa55555bbb"
output = ""

for ch in input_str:
    if ch >= '0' and ch <= '9':
        output += '*'
    else:
        output += ch
print(output)