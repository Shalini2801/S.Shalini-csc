 # In strings we can write in both double and single quotes
    print("30 days 30 challenges")
    print('30 days 30 challenges')
30 days 30 challenges
30 days 30 challenges

#Assigning String to Variable:
Hours = "thirty"
print(Hours)
thirty


# indexing using String :
Days="Thirty days"
print(Days[0])
print(Days[1])
print(Days[2])
print(Days[3])
print(Days[4])
print(Days[5])
print(Days[6])
T
h
i
r
t
y
 

# Range of index in the string
challenge="I will win"
print(challenge[0:6])
print(challenge[0:])
print(challenge[:6])
print(challenge[-1:])
print(challenge[:-1])
i will
i will win
i will
n
i will wi


# length of characters
challenge = "I will win"
print(len(challenge))
10


#strings in lower case
challenge="I will win"
print(challenge.lower())
i will win



#strings in upper case
challenge="I will win"
print(challenge.upper())
I WILL WIN



#string concatenation-joining two words
a="30 Days"
b="30 Challenges"
c= a + b
print(c)
30 Days30 Challenges



# Adding space during concatenation 
a="30 Days"
b="30 Challenges"
c= a + " " + b
print(c)
30 Days 30 Challenges



#casefold()-usage
text="30 days 30 challenges"
x=text.casefold()
print(x)
30 days 30 challenges



#capitalize-Upper case the first letter in this sentence
text="30 days 30 challenges"
print(text.capitalize())
30 days 30 challenges

#find-used to find a word in the sentence
text="30 days 30 challenges"
x=text.find("days")
print(x)
3


#isalpha()-returns True if all the characters are alphabet letters (a-z)
text="30 days 30 challenges"
x=text.isalpha()
print(x)
False

#isalnum()-returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
text="30 days 30 challenges"
x=text.isalnum()
print(x)
False