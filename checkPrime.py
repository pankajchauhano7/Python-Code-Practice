def Prime(num): #Check Prime
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
    
num=4
if Prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")
        