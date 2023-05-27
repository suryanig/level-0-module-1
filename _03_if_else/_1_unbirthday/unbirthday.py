
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    birthday = simpledialog.askstring(title='What is your birthday?', prompt="Please give me your birthday as mm/dd.")
    if birthday == "05/19":
        messagebox.showinfo(title='Today is your birthday!', message="Happy Birthday!")
    else:
        messagebox.showinfo(title='Today is not your birthday', message="Happy Un-Birthday!")
