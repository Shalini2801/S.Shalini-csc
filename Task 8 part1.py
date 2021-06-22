print("******* Task 8 from 1-5 *******\n")
print("1.Write a Python script to merge two Python dictionaries")
dict1={"a":"150","b":"110","c":"100"}
dict2={"d":"100","e":"110","f":"90"}
print(dict1)
print(dict2)
res={*dict1,*dict2}
print("Dictionaries after merging",res)
print("\n2.Write a program to sort the value from descending to ascending in list and convert it in to a set.")
lst=[10,9,12,11,4,0,3]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
print("\nList into set: ")
s=set(lst)
print(s)
print(type(s))
print(type(lst))
print("\n3.Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.")
dict1={"Shalini":[99,98,92,90],"Ganesh":[100,99,98,99],"Ram":[95,96,95,99]}
result={k:sorted(dict1[k]) for k in sorted(dict1)}
print(result)
def function1(dict1):
    res = dict()
    for key in sorted(dict1):
        res[key] = sorted(dict1[key])
    return res
function1(dict1)

def function2(dict1):
    res=dict()
    min1=dict1[key]
    for key in sorted(dict1):
        if dict1[key]<min1:
            min1=dict1[key]
            res[key]=min1
    return res
function1(dict1)
print("\n4.Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input")
def string():
    user=input("Enter the string :")
    word="String is given by user "
    return user+word[6:]
print(string())
def string1():
    user=input("Enter the string :")
    word="\nString is given by user  "
    return word.replace('String',user)
print(string1())
print("\n5.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.")
def fun():
    user=input("Enter a string:")
    return user.capitalize()
print(fun())
str="stay safe,take care"
print(str.title())
print("----------Task 8  from 1-5 completed-----------")