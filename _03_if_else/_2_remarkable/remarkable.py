from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    name = simpledialog.askstring(title = 'Name', prompt = "Please enter the name of someone in your class to find out something remarkable about them.")
    if name == "Aryahi":
        messagebox.showinfo(title='Aryahi', message = "Aryahi is remarkable because she has the best sister in the world.")
    if name == "Suryani":
        messagebox.showinfo(title = 'Suryani', message = "Suryani is remarkable because she just is.")
    else:
        messagebox.showinfo(title = 'Hmmmmm', message = "Hmmmmmm. I'm sorry. I don't know who that is")
