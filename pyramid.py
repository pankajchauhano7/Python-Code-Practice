height=5
#Upward pyramid
#for i in range(1, height+1):
    # Print leading spaces to center the stars
#    print(" "*(height-i),end="")
    # Print stars
#    print("*"*(2*i-1))
    
#Downward pyramid
for i in range(height+1,0,-1):
    # Print leading spaces to center the stars
    print(" "*(height-i),end=" ")
    # Print stars
    print("*"*(2*i-1))
    

    