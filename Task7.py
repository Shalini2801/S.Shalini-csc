print("********Task 7 Functions********")
print("1. Create a function getting two integer inputs from user.& print the following:\nAddition of two numbers is +value\nSubtraction of two numbers is +value\nDivision of two numbers is +value\nMultiplication of two numbers is +value")
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
symbol=input("Enter '+' for addition,'-' for subtraction,'*' for multiplication,'/ for division': ")

def math_function(a,b,sign):
  if sign== '+':
        print("Addition of a and b is ",str(a+b))
  elif sign== '-':
        print("Subraction of a and b is ",str(a-b)) 
  elif sign == '*':
        print("Multiplication of a and b is ",str(a*b))
  elif sign == '/':
        print("Division of a and b is ",str(a/b))
math_function(a,b,symbol)

print("\n2.Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree")
def covid(name,temp):
 print("Enter the name : ",name)
 if temp=='':
  print("Temp is : 98")
 else:
  print("Temp is : ",temp)
name = input("Enter name : ")
temp=input("Enter temp : ")
covid(name,temp)
print("\n------------Task 7 Completed-----------")