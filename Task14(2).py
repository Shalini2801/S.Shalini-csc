#2.Design a simple calculator app with try and except for all use cases
def calculate():
    try:
        print('+')
        print('-')
        print('*')
        print('/')
        print('%')
        print('**')
        operation = input("Select an operator:")
        print("Enter two numbers")
        number_1 = int(input())
        number_2 = int(input())
        if operation == '+': 
            print(number_1 + number_2)
        elif operation == '-': 
            print(number_1 - number_2)
        elif operation == '*': 
            print(number_1 * number_2)
        elif operation == '/': 
            print(number_1 / number_2)
        elif operation == '%': 
            print(number_1 % number_2)
        elif operation == '**': 
            print(number_1 ** number_2)
        else:
            print('Invalid Input')
    except Exception as e:
        print(e)
calculate()
   
#Output
+
-
*
/
%
**
Select an operator : +
Enter two numbers
10
10
20
