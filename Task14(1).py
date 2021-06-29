#1.List down all the error types and check all the errors using a python program for all errors
print("Some Python errors are 1. Name error\n"
      "2. Type error\n"
      "3.Value error\n"
      "4.Index error\n"
      "5.Zero division error")
print("1.Name error")
age
print(age)

#Error
NameError: name 'age' is not defined

print("2. Type error")
a = "abc"+123
print(a)

#Error
TypeError: can only concatenate str (not "int") to str

print("3.value error")
int("123")

#Error
ValueError: invalid literal for int()

print("4.index number")
list = [1,2,3]
print(list[3])

#Error
IndexError: list index out of range

print("5.zero division error")
a = 1
b= 0
print(a/b)

#Error
ZeroDivisionError: division by zero