"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(title='Number 1', prompt="Can you please enter 1 number")
    num2 = simpledialog.askinteger(title='Number 2', prompt="Can you please enter another number")
    sum = num1 + num2
    messagebox.showinfo(message = "The sum of those 2 numbers are " + str(sum))
