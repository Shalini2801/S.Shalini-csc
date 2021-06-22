print("***********Task 9************")
print("1.Write a program to loop through a list of numbers and add +2 to every value to elements in list")
lst=[1,2,3,4,5,6,7,8,9,10]
result=[]
for i in lst:
    result.append(i+2)
print(result)
print("\n2.Write a program to get the below pattern:\n54321\n4321\n321\n21\n1\n")
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()    
print("\n3.Python Program to Print the Fibonacci sequence")
def fibo(n):
    n1, n2 = 0, 1
    count = 0
    if n == 1 or n == 2:
        print('1')
    else :
         while count < n:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
print(fibo(12))
print("\n4.Explain Armstrong number and write a code with a function")
print("Armstrong number :A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.\n")
n = int(input('enter a number: '))
temp = n
sum =0
while(n>0):
    n1=n%10
    sum=sum + n1**3
    n = n//10
if(sum == temp):
 print(temp,"is armstrong")
else :
 print(temp,"is not armstrong")
print("\n5.Write a program to print the multiplication table of 9")
for x in range(1,11):
    print("9x",x,'=',x*9 ) 
print("\n6.Check if a program is negative or positive")
x=[10,-10,20,-56,+56,45]
for i in x:
    if i>=0:
        print(i,"is positive")
    else:
        print(i,"is negative")
print("\n7.Write a program to convert the number of days to ages")
def find( number_of_days ):
    year = int(number_of_days / 365)
    print(year,'Years ago !')
no_days=600
find(no_days)
no_days=2000
find(no_days)
print("\n8.Solve Trigonometry problem using math function write a program to solve using math function")

import math
def trigo(n,m):
    if n=='sin':
        return math.sin(m)
    elif n=='cos':
        return math.cos(m)
    elif n=='cosin':
        return math.cosine(m)
    elif n=='tan':
        return math.tan(m)
    elif n=='sec':
        return math.sec(m)
    elif n=='cosec':
        return math.cosec(m)     
print(trigo('sin',30))
print(trigo('tan',30))
print(trigo('cos',90))
print("\n9.Create a calculator only on a code level by using if condition (Basic arithmetic calculation)")
ch ='yes'
while(ch=='yes'):
    print("Select operation.")
    print("1.Add (+) ")
    print("2.Subtract (-) ")
    print("3.Multiply (*) ")
    print("4.Divide (/) ")
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '+':
            print(num1,"+",num2,"=",num1+num2)
        elif choice == '-':
            print(num1, "-", num2, "=", num1 - num2)
        elif choice == '*':
            print(num1, "*", num2, "=", num1 * num2)
        elif choice == '/':
            print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Invalid Input")
    ch= input("Do you want to continue enter your choice yes/no :")
print("end")
print("---------------Task 9 Completed-------------")