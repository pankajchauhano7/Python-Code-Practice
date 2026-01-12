# Program to check if a number is a Fibonacci number or return the largest Fibonacci number 
# less than n
n=10
def check_fibo(n):
    a,b=0,1
    while b<n:
        a,b=b,a+b
    if n == a:
        return n
    else:
        return a
print(check_fibo(n))    


