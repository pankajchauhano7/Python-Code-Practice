str = "my name is pankaj"
words=str.split()
rev_str=" ".join(word[::-1] for word in words)
print(rev_str)
