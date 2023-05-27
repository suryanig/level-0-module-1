# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import math
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    radius = simpledialog.askinteger(title = 'radius', prompt = "What would you like the radius of your circle to be?")
    circle = simpledialog.askstring(title = 'Area or Circumference?', prompt = "Would you like to find the area or circumference of that?")
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    if circle == "area":
        messagebox.showinfo(title="Here is the area of your circle:", message = area)
    if circle == "circumference":
        messagebox.showinfo(title="Here is the circumference of your circle:", message = circumference)
#Area = πr^2
#Circumference = 2πr 
