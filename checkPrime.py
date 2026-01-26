#Check Prime
def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True
    
num=633
if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")
        