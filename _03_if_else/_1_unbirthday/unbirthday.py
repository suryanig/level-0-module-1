
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':

    birthday = simpledialog.askstring(title='What is your birthday?', prompt = "Please give me your birthday as mm/dd.")
    if birthday == "5/19":
        messagebox.showinfo()
