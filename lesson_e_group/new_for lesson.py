from tkinter import *

root = Tk()
data = 0
action = ""


def number(digit: str):
    global enter
    enter.insert(index=END, string=digit)


def fun_plus():
    global action, data
    data += int(enter.get())
    action += "plus"
    enter.delete(0, END)


def fun_equal():
    global data, action
    if action == "plus":
        print(data)
        print(enter.get())
        data += int(enter.get())
    elif action == "minus":
        data -= int(enter.get())
    enter.delete(0, END)
    enter.insert(END, str(data))


enter = Entry()
enter.pack()

button = Button(text="1", command=lambda: number("1"))
button.pack()
button2 = Button(text="2", command=lambda: number("2"))
button2.pack()

plus = Button(text="+", command=fun_plus)
plus.pack()
equal = Button(text="=", command=fun_equal)
equal.pack()
mainloop()
