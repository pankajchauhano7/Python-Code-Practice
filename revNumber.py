# Reverse a number
num=1234
revNum=0
while num !=0:
    rem=num%10
    revNum = revNum*10+rem
    num=num//10
print(revNum)
