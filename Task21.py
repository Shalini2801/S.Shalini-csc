print("******Task 21***********\n")
print("\n1.using merging two list using zip")
t1=(1,2,3,4,5)
t2=(6,7,8,9)
l=zip(t1,t2)
print(list(l))



print("\n2.mergening range and list")
r=range(1,8)
l=[10,20,30,40,50,60,70]
x=zip(r,l)
print(tuple(x))



print("\n3.sorting list using sorted")
l=[9,7,4,8,3,1,2,6,5]
l1=sorted(l)
print(l1)




print("\n4.filtering even number from list and displayind odd numbers")
def iseven(x):
    if x%2==0:
        return True
    else :
        return False

l=[1,2,3,4,5,6,7,8,9]
even=list(filter(iseven,l))
print(even)
l1=[]
for i in l:
    if i not in even:
       l1.append(i)
print(l1)    
print("\n*********Task completed******")