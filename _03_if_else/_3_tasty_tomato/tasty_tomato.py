from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color = simpledialog.askstring(title = 'Color', prompt = "Choose from red, green, and yellow for the tomato color.")

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if color == "red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if color == "green":
    canvas.create_oval(75, 200, 400, 450, fill="yellow green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="yellow green", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if color == "yellow":
    canvas.create_oval(75, 200, 400, 450, fill="gold", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="gold", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
else:
    messagebox.showinfo(title='Ummmm', message= "Hate to break it to you, but tomatoes don't come in that color.")
root.mainloop()
