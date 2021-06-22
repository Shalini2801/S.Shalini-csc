print("*********Task 8 from 6-10************")
print("\n6.Write a Python program to find the repeated items of a list")
from collections import Counter
L1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(L1)
print(d)
new_list = list([item for item in d if d[item]>1])
print(new_list)
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
list1 = [100, 250, 350, 250, 250, 350, 410,
         550, -220, 600, 600, -250, -250]
print (Repeat(list1))
print("\n7.Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user ")
a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
sum=a+b+c
print("Sum : ",sum)
user=int(input("Enter the number to divide sum"))
if sum%user==0:
    print("The given input divide")
else :
    print("The given input does not divide sum1")
print("\n8.Write a Python program to find the Mean,median,mode among three given numbers")    
given_numbers = [1,2,2]
addition = 0
for i in given_numbers:
    addition=addition+i
print("addition",addition)
length = len(given_numbers)
mean = addition/length
print("mean :",mean)

given_numbers.sort()
if length%2==0:
    median1 = given_numbers[length//2]
    median2=given_numbers[length//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[length//2]
print("median is:",median)
import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)    
print("\n9.Write a Python program to swap cases of a given string")
a="Shalini"
b="Hi"
tep=a
a=b
b=tep
print(a,b)
x = a
y = b
x, y = y, x
print(x,y)
print("\n10.Write a program to convert an integer to binary & octa decimal")
def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")
n=65
decToOctal(n)
n=3
decToOctal(n)
print("\n*********Task 8 from 6-10 Completed ************")