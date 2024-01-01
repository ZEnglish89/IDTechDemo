
x = int(input("Please enter an integer: "))

print("Your input is: " + str(x))

if(x%2==0):
    print("Your input was even")
else:
    print("Your input was odd")

if(x>-10 and x<10):
    print("You inputted a single-digit number")
elif(x>-100 and x<100):
    print("You inputted a double-digit number")
else:
    print("Your inputted number had more than two digits")

if(x==8 or x==15):
    print("You inputted a lucky number!")