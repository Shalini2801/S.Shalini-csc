# import all prerequisite
from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter import messagebox
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger,PageRange


root = Tk()

# naming the GUI interface to image_conversion_APP
root.title("APP by Magendra")

def merger():
	global pdf1,pdf2
	import1=fd.askopenfilename()
	pdf1=PdfFileReader(import1)
	import2=fd.askopenfilename()
	pdf2=PdfFileReader(import2)

	obj=PdfFileMerger()
	obj.append(pdf1,'rb')
	obj.append(pdf2,'rb')
	obj.write('mergedpdf.PDF')



# creating the Function which converts the jpg_to_png
def jpg_to_png():
	global im1

	# import the image from the folder
	import_filename = fd.askopenfilename()
	if import_filename.endswith(".jpg"):

		im1 = Image.open(import_filename)

		# after converting the image save to desired
		# location with the Extersion .png
		export_filename = fd.asksaveasfilename(defaultextension=".png")
		im1.save(export_filename)

		# displaying the Messaging box with the Success
		messagebox.showinfo("success ", "your Image converted to Png")
	else:

		# if Image select is not with the Format of .jpg
		# then display the Error
		Label_2 = Label(root, text="Error!", width=20,
						fg="red", font=("bold", 15))
		Label_2.place(x=80, y=280)
		messagebox.showerror("Fail!!", "Something Went Wrong...")

def weather():
    a=citys.get()

    print("weather in ",a,)
    print("Max temperature : 37 celcius")
    print("Min temperature : 27 celcius")
    print("Partly cloudy")
    print("chances of rain 25%")





button1 = Button(root, text="JPG_to_PNG", width=10, height=1, bg="green",
				fg="white", font=("helvetica", 10, "bold"), command=jpg_to_png)

button1.grid(column=1,row=1)

citys=StringVar()

city=Label(root,text="city name").grid(column=1,row=3)
city=Entry(root,textvariable=citys).grid(column=2,row=3)


button2=Button(root,text="fetch weather",width=10,height=1,bg='blue',fg="white",font=('helvetica',10,'bold'),command=weather)
button2.grid(column=1,row=5)


button3=Button(root,text="pdf merger",width=10,height=1,bg='red',fg='white',font=('helvetica',10,'bold'),command=merger)
button3.grid(column=1,row=6)

root.geometry("500x500+400+200")
root.mainloop()