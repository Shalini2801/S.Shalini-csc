from tkinter import *
from tkinter import ttk
root = Tk()
root.title("EmployeeRegistration Form")
root.geometry('400x300')
root.configure(background = "LemonChiffon1");
EmployeeFirstname = Label(root ,text = "Employee First Name").grid(row = 0,column = 0)
EmployeeLastName = Label(root ,text = "Employee Last Name").grid(row = 1,column = 0)
EmployeesID= Label(root ,text = "Employee ID").grid(row = 2,column = 0)
DateOfBirth= Label(root ,text = "Employee D.O.B").grid(row =3,column = 0)
Address= Label(root ,text = "Employee’s Address").grid(row =4,column = 0)
Pincode=Label(root,text="Pincode").grid(row=5,column=0)
State=Label(root ,text = "State").grid(row =6,column = 0)
City=Label(root ,text = "City").grid(row =7,column = 0)
Email = Label(root ,text = "Email Id").grid(row = 8,column = 0)
Mobile = Label(root ,text = "Contact Number").grid(row = 9,column = 0)
Submit=Label(root ,text = "Submitted").grid(row = 10,column=1)
variable=IntVar()

# This will creates checkbutton widget and uses place() method.
Checkbutton(root,text="I Accept all Term and Conditions", variable=variable).place(x=148,y=455)

EmployeeFirstname1 = Entry(root).grid(row = 0,column = 1)
EmployeeLastname1 = Entry(root).grid(row = 1,column = 1)
EmployeeID1= Entry(root).grid(row =2,column = 1)
DateOfBirth1= Entry(root).grid(row =3,column = 1)
Address1= Entry(root).grid(row =4,column = 1)
Pincode1=Entry(root).grid(row =5,column = 1)
State1=Entry(root).grid(row =6,column = 1)
City1=Entry(root).grid(row =7,column = 1)
Email1 = Entry(root).grid(row =8,column = 1)
Mobile1 = Entry(root).grid(row = 9,column = 1)
Submit1=Entry(root).grid(row = 15,column=56)

def clicked():
 Button(root, text="Submit", command=clicked,width=5).grid(row = 4,column = 2)
root.mainloop()