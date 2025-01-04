a = [(1, 2, "Pankaj", "Sayan"), (1, 2), ("Mukul", "Ravi"), ("Achin", 3, 4, "Anku")]
new_a = []
for i in a:
    for item in i:
        if isinstance(item, str):
            new_a.append(item)
            # new_a = list(set(new_a)) //remove duplicate values

print(new_a)
