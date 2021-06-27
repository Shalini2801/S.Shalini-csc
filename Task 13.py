print("**********Task 13**********")
print("\n1.Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).")
import re
def a_char(string):
 charRe = re.compile(r'[^a-zA-Z0-9.]')
 string = charRe.search(string)   
 return not bool(string)
print(a_char("jan2930"))
print(a_char("&%@#!}{"))
print("\n")
print("2.Write a Python program that matches a word containing 'ab'")
import re
str=input('\n\nEnter a string:')
res=re.findall(r'ab\w*',str)
print("\n",res)
print("\n3.Write a Python program to check for a number at the end of a word/sentence.\n")
import re
str='day13,Task30'
res=re.findall(r'\w*\d',str)
for i in res:
	print( i)
print("\n4.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string\n")
import re
output= re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in output:
     print(n.group(0))
print("\n5.Write a Python program to match a string that contains only uppercase letters\n")
import re
str=input("Enter string:")
res=re.findall(r'\w[A-Z]\w',str)
print(res)
print("\n--------------------Task 13 Completed------------------")