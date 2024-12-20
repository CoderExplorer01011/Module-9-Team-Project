# This program involves a calculator that displays a GUI for easier user interaction
# Updated on: 11/24/2024
# Updated by: James, David R


# Document what the following lines of code do here
# Imports all classes and functions from the tkinter library for creating GUI applications
from tkinter import * 
# Creates a main window (root) for the GUI
root = Tk()
# Sets the title of the main window to "Simple Calculator"
root.title("Simple Calculator")

# Document what the following lines of code do here
e = Entry(root, width=35, borderwidth=5)  # Creates an input field (Entry widget) in the root window
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Places the input field at row 0, column 0, spanning 3 columns, with padding

# Document what the following lines of code do here
def button_click(number):  # Defines a function that will be triggered when a number button is clicked
    current = e.get()  # Gets the current value from the input field
    e.delete(0, END)  # Clears the input field
    e.insert(0, str(current) + str(number))  # Inserts the clicked number at the end of the current value in the input field

# Document what the following lines of code do here
def button_clear():  # Defines a function to clear the input field when the "Clear" button is clicked
    e.delete(0, END)  # Clears the content of the input field

# Document what the following lines of code do here
def button_operator(operator):  # Defines a function for handling operations like +, -, *, /
    first_number = e.get()  # Gets the current value from the input field
    global f_num  # Declares a global variable f_num to store the first number
    global num_operator  # Declares a global variable to store the selected operator
    f_num = int(first_number)  # Stores the first number as an integer
    num_operator = operator  # Stores the operator
    e.delete(0, END)  # Clears the input field

# Document what the following lines of code do here
def button_equal():  # Defines a function that calculates the result when "=" is clicked
    second_number = e.get()  # Gets the second number from the input field
    e.delete(0, END)  # Clears the input field
    if num_operator == '+':  # If the operator is '+', add the numbers
        e.insert(0, f_num + int(second_number))  # Adds f_num and second_number, displays the result
    elif num_operator == '*':  # If the operator is '*', multiply the numbers
        e.insert(0, f_num * int(second_number))  # Multiplies f_num and second_number, displays the result
    elif num_operator == '/':  # If the operator is '/', divide the numbers
        e.insert(0, f_num / int(second_number))  # Divides f_num by second_number, displays the result
    elif num_operator == '-':  # If the operator is '-', subtract the numbers
        e.insert(0, f_num - int(second_number))  # Subtracts second_number from f_num, displays the result
    else:  # If no valid operator is selected
        e.insert(0, "Invalid!!!")  # Displays an error message

# Document what the following lines of code do here

# NOTE: We did not cover Lambda functions in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))  # Creates a button labeled "1" and links it to the button_click function
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))  # Creates a button labeled "2" and links it to the button_click function
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))  # Creates a button labeled "3" and links it to the button_click function
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))  # Creates a button labeled "4" and links it to the button_click function
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))  # Creates a button labeled "5" and links it to the button_click function
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))  # Creates a button labeled "6" and links it to the button_click function
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))  # Creates a button labeled "7" and links it to the button_click function
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))  # Creates a button labeled "8" and links it to the button_click function
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))  # Creates a button labeled "9" and links it to the button_click function
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))  # Creates a button labeled "0" and links it to the button_click function
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))  # Creates a button labeled "+" and links it to the button_operator function
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)  # Creates a button labeled "=" and links it to the button_equal function
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)  # Creates a button labeled "Clear" and links it to the button_clear function

# Document what the following lines of code do here
# See the description of a Lambda function above

# The lines of code provided, show up in the GUI application, if not included it wouldn't show up and defeat the purpose of a calculator
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
# This line of code creates a button for subtraction, links it to 'button_operator'
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
# This line of code creates a button for multiplication, links it to 'button_operator'
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))
# This line of code creates a button for division, links it to 'button_operator'

# Document what the following lines of code do here

# The code below shows, organization within the GUI application, their positioning can be altered if a coder is not satifated with the look by adjusting the rows and columns
# The code mentions 'grid' which helps with organizing but in a grid form starting at zero
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
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)


button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


# Document what the following line of code do here
# This line of code keeps the application running until the user closes the application
root.mainloop()
