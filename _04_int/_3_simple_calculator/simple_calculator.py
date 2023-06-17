"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(title='Number 1', prompt="Can you please enter 1 number")
    num2 = simpledialog.askinteger(title='Number 2', prompt="Can you please enter another number")
    operation = simpledialog.askstring(title= "Which Operation?", prompt = "Do you want to add, subtract, multiply, or divide those two numbers?")
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quot = num1 / num2
    if operation == "add":
        messagebox.showinfo(message = "The sum of those 2 numbers are " + str(sum))
    elif operation == "subtract":
        messagebox.showinfo(message = "The difference of those 2 numbers are " + str(diff))
    elif operation == "multiply":
        messagebox.showinfo(message = "The product of those 2 numbers are " + str(prod))
    elif operation == "divide":
        messagebox.showinfo(message = "The quotient of those 2 numbers are " + str(quot))
    else:
        messagebox.showinfo(message = "Sorry, I don't know how to do that")
