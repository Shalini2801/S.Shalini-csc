print("*******Task 6- Dictionary,Sets*******\n")
print("1.Write a Python script to merge two Python dictionaries")
dict1={"Sachin":"150","Kholi":"110","Virat":"100"}
dict2={"Sehwag":"100","Jadeja":"110","Shami":"90"}
print(dict1)
print(dict2)
res={**dict1,**dict2}
print("Dictionaries after merging\n",res)

print("\n2.Write a Python program to remove a key from a dictionary")
dict1.pop("Virat")
print(dict1)

print("\n3.Write a Python program to map two lists into a dictionary")
M1=["Rama","Ragav","Ganesh"]
M2=[1,2,3]
res={}
for key in M1:
    for value in M2:
        res[key]=value
        M2.remove(value)
        break
print("Dictionary",str(res))
print("\n4.Write a Python program to find the length of a set")
print("Length of the dictionary is:",len(M1))
print("\n5.Write a Python program to remove the intersection of a 2nd set from the 1st set")
m1={1,2,3,4,5,6,7,8,9,10}
m2={7,8,9,10,11,12,13,14}
print(m2.intersection(m1))
print("\n************Task 6 Completed**************")