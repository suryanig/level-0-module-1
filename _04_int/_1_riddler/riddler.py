"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
    rid1 = simpledialog.askstring(title = 'Here is your first riddle:', prompt = "What has to be broken before you can use it?")
    if rid1 == "an egg":
        score = score + 1
    rid2 = simpledialog.askstring(title = 'Here is your second riddle:', prompt = "I’m tall when I’m young, and I’m short when I’m old. What am I?")
    if rid2 == "a candle":
        score = score + 1
    rid3 = simpledialog.askstring(title = 'Here is your third and last riddle:', prompt = "What month of the year has 28 days?")
    if rid3 == "all of them":
        score = score + 1

    messagebox.showinfo(message = "Yay! You got " + str(score) + " out of 3 points.")
