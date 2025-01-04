def gcd(a,b):
    smallest=min(a,b)
    for i in range(smallest,0,-1):
        if a%i == 0 and b%i == 0:
            return i
        
gcd_value = gcd(36,60)
print(gcd_value)