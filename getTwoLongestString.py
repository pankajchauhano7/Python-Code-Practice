#Find two largest string from list
str1 = ["Pankaj", "Ravi", "Mukul", "Rajat"]

lstr1 = ""
lstr2 = ""

for s in str1:
    if len(s) > len(lstr1):
        lstr2 = lstr1
        lstr1 = s
    else:
        if len(s) > len(lstr2):
            lstr2 = s
print(lstr1, lstr2)
