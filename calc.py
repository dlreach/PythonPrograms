from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

	# Button Functions

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)

	if math == "addition":
		e.insert(0, f_num + float(second_number))

	if math == "subtraction":
		e.insert(0, f_num - float(second_number))

	if math == "multiplication":
		e.insert(0, f_num * float(second_number))

	if math == "division":
		e.insert(0, f_num / float(second_number))

	if math == "square":
		e.insert(0, f_num ** 2)

	if math == "sqrt":
		e.insert(0, f_num ** 0.5)

	if math == "plusminus":
		e.insert(0, f_num * -1)

	if math == "percent":
		e.insert(0, 1/f_num)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = float(first_number)
	e.delete(0, END)

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = float(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = float(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = float(first_number)
	e.delete(0, END)

def button_square():
	first_number = e.get()
	global f_num
	global math
	math = "square"
	f_num = float(first_number)
	e.delete(0, END)


def button_percent():
	first_number = e.get()
	global f_num
	global math
	math = "percent"
	f_num = float(first_number)
	e.delete(0, END)
	#e.insert(0, f_num / 100)

def button_sqrt():
	first_number = e.get()
	global f_num
	global math
	math = "sqrt"
	f_num = float(first_number)
	e.delete(0, END)

def button_plusminus():
	first_number = e.get()
	global f_num
	global math
	math = "plusminus"
	f_num = float(first_number)
	e.delete(0, END)



# Define buttons

button_1 = Button(root, text="1", padx=40, pady=20, bg="pale green", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="pale green", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="pale green", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="pale green", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="pale green", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="pale green", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="pale green", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="pale green", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="pale green", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="pale green", command=lambda: button_click(0))
button_percent = Button(root, text="%", padx=38, pady=20, bg="red", command=button_percent)
button_clear = Button(root, text="Clear", padx=29, pady=20, bg="red", command=button_clear)
button_add = Button(root, text="+", padx=40, pady=20, bg="sky blue", command=button_add)
button_divide = Button(root, text="/", padx=40, pady=20, bg= "sky blue", command=button_divide)
button_square = Button(root, text="x^2 ", padx=31, pady=20, bg="red", command=button_square)
button_subtract = Button(root, text="-", padx=41, pady=20, bg="sky blue", command=button_subtract)
button_multiply = Button(root, text="*", padx=40.5, pady=20, bg="sky blue", command=button_multiply)
button_plusminus = Button(root, text="+/-", padx=33, pady=20, bg="red", command=button_plusminus)
button_sqrt = Button(root, text="sqrt ", padx=32, pady=20, bg="red", command=button_sqrt)
button_equal = Button(root, text="=", padx=86, pady=20, bg="yellow", command=button_equal)

# Put buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_percent.grid(row=4,column=1)
button_clear.grid(row=4, column=2)


button_add.grid(row=5, column=0)
button_square.grid(row=5, column=2)
button_divide.grid(row=5, column=1)



button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_plusminus.grid(row=6, column=2)

button_sqrt.grid(row=7, column=0)
button_equal.grid(row=7, columnspan = 2, column=1) #columnspan() to make wider


root.mainloop()
