print("**************Task 16**********\n")
print("1.Create a lambda function that multiplies argument x with argument y")
r=lambda x,y:x*y
result=r(10,10)
print("\n",result)
print("\n2.Write a Python program to create Fibonacci series to n using Lambda")
from functools import reduce
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],range(n - 2), [0, 1])
print(fib(10))
print("\n3.Write a Python program that multiply each number of given list with a given number ")
nums = [2, 4, 6, 3 ,10]
n = 3
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))
print("\n4.Write a Python program to find numbers divisible by 9 from a list of numbers")
lst = [1,9,18,3,27,81,8,20]
result = list(filter(lambda x: (x %9== 0),lst))
print("\nNumbers divisible by 9 are",result)
print("\n5.Write a Python program to count the even numbers in a given list of integers ")
lst=[10,2,4,33,22,28,30]
print(lst)
lst1=list(filter(lambda j:j%2==0,lst))
print("Result :")
print(len(lst1))
print("\n**********Task 16 Completed***********")