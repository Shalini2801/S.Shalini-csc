#4.When try-except scenario is not required?
print("4.try catch is needed only if expected error is small and does not affect the program, in case of fatal errors try catch block is not recommended\n")
#5.Try getting an input inside the try catch block
try:
    n=int(input("\nEnter a number"))
    print(n)
except:
    print("Invalid")