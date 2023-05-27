import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    mrgreen = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='Shape', prompt="What shape do you want to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "triangle":
        for i in range (3):
            mrgreen.forward(100)
            mrgreen.right(120)
    elif shape == "square":
        for i in range (4):
            mrgreen.forward(100)
            mrgreen.right(90)
    elif shape == "circle":
        mrgreen.circle(100)
    else:
        messagebox.showinfo(message="Sorry, I don't know how to draw that shape.")
    # Call the turtle .done() method
