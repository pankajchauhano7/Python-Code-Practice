str="MOM"
revStr=""
for ch in str:
    revStr=ch+revStr
if str == revStr:
    print("Palindrome")
else:
    print("Not a Palindrome")
