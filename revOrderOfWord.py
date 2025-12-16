s = "Pankaj is awesome"
words = []
word = ""
# split manually
for ch in s:
    if ch != " ":
        word += ch
    else:
        words.append(word)
        word = ""
# add last word
words.append(word)
# reverse words manually
new_s = ""
for i in range(len(words) - 1, -1, -1):
    new_s += words[i]
    if i != 0:
        new_s += " "
print(new_s)
