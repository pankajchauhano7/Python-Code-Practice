def test(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst

print(test(1))
print(test(2))
print(test(2,[10,20]))
print(test(4))