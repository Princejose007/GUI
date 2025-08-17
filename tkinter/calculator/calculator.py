from tkinter import *

# Calculator functions
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, END)

def button_operation(op):
    global first_number
    global operation
    operation = op
    first_number = float(display.get())
    display.delete(0, END)

def button_equal():
    second_number = float(display.get())
    display.delete(0, END)
    
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    
    display.insert(0, str(result))

# Memory functions
def memory_add():
    global memory
    if display.get():
        memory += float(display.get())

def memory_subtract():
    global memory
    if display.get():
        memory -= float(display.get())

def memory_recall():
    display.delete(0, END)
    display.insert(0, str(memory))

def memory_clear():
    global memory
    memory = 0

# Create main window
root = Tk()
root.title("Enhanced Calculator")
root.geometry('300x450')
root.config(bg='lightblue')

# Initialize memory
memory = 0

# Display
display = Entry(root, width=20, font=('Arial', 16), borderwidth=5, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Number buttons
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1), bg='white')
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2), bg='white')
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3), bg='white')
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4), bg='white')
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5), bg='white')
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6), bg='white')
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7), bg='white')
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8), bg='white')
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9), bg='white')
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0), bg='white')

# Operation buttons
button_add = Button(root, text="+", padx=29, pady=20, command=lambda: button_operation("+"), bg='lightgray')
button_sub = Button(root, text="-", padx=30, pady=20, command=lambda: button_operation("-"), bg='lightgray')
button_mul = Button(root, text="×", padx=30, pady=20, command=lambda: button_operation("*"), bg='lightgray')
button_div = Button(root, text="÷", padx=30, pady=20, command=lambda: button_operation("/"), bg='lightgray')

button_equal = Button(root, text="=", padx=29, pady=20, command=button_equal, bg='orange')
button_clear = Button(root, text="C", padx=29, pady=20, command=button_clear, bg='orange')

# Memory buttons
button_mplus = Button(root, text="M+", padx=24, pady=20, command=memory_add, bg='lightgreen')
button_mminus = Button(root, text="M-", padx=24, pady=20, command=memory_subtract, bg='lightgreen')
button_mr = Button(root, text="MR", padx=23, pady=20, command=memory_recall, bg='lightgreen')
button_mc = Button(root, text="MC", padx=23, pady=20, command=memory_clear, bg='lightgreen')

# Arrange buttons on grid
# First row (memory buttons)
button_mplus.grid(row=1, column=0)
button_mminus.grid(row=1, column=1)
button_mr.grid(row=1, column=2)
button_mc.grid(row=1, column=3)

# Number buttons
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_div.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_sub.grid(row=4, column=3)

button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_add.grid(row=5, column=3)

root.mainloop()
