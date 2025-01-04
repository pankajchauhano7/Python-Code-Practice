s="abcabcbb"
start=0
max_len=0
seen_chars=set()

for end in range(len(s)):
    while s[end] in seen_chars:
        seen_chars.remove(s[start])
        start +=1
    seen_chars.add(s[end])
    max_len=max(max_len,end-start+1)
print(max_len)