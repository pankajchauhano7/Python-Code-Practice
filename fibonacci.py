nterms = int(input("How many terms? "))
n1=0
n2=1
c=0
if nterms <= 0:
    print("enter a positive number")
elif nterms == 1:
    print("Fibonacci series upto : "+nterms+":")
    print(nterms)
else:
    print("Fibonacci series :")
    while c<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1

