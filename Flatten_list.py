a=[1,[2,[3,4],6]]


def flatten(a):
    new_a=[]
    for i in a:
        if isinstance(i,list):
            new_a.extend(flatten(i))
        else:
            new_a.append(i)
    return new_a

print(flatten(a))

