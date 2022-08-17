from tkinter import *

root = Tk()
root.geometry("350x430")
root.title("CALCULATOR")
root.resizable(False, False)
frame = Frame()
frame.place(x=0, y=50)
data = 0
action = ""
entry = Entry(justify=RIGHT)
entry.config(font=("impact", 27), bd=3)
entry.place(x=0, y=0, width=350)


def fun(num: str):
    global entry
    entry.insert(END, num)


def fun_plus():
    global entry, data, action
    data += int(entry.get())
    action += "plus"
    entry.delete(0, END)


def fun_minus():
    global entry, data, action
    data += int(entry.get())
    action += "minus"
    entry.delete(0, END)


def fun_multiply():
    global entry, data, action
    data += int(entry.get())
    action += "multiply"
    entry.delete(0, END)


def fun_divide():
    global entry, data, action
    data += int(entry.get())
    action += "divide"
    entry.delete(0, END)


def fun_equal():
    global data, entry, action
    if action == "plus":
        data += int(entry.get())
    elif action == "minus":
        data -= int(entry.get())
    elif action == "multiply":
        data *= int(entry.get())
    else:
        data /= int(entry.get())
    entry.delete(0, END)
    entry.insert(END, str(data))
    data -= data
    action = ""


num0 = Button(frame, text="0", command=lambda: fun("0"))
num0.place(x=0, y=285, width=174, height=95)
num1 = Button(frame, text="1", command=lambda: fun("1"))
num1.grid(row=2, column=0, ipadx=35, ipady=35)
num2 = Button(frame, text="2", command=lambda: fun("2"))
num2.grid(row=2, column=1, ipadx=35, ipady=35)
num3 = Button(frame, text="3", command=lambda: fun("3"))
num3.grid(row=2, column=2, ipadx=35, ipady=35)
num4 = Button(frame, text="4", command=lambda: fun("4"))
num4.grid(row=1, column=0, ipadx=35, ipady=35)
num5 = Button(frame, text="5", command=lambda: fun("5"))
num5.grid(row=1, column=1, ipadx=35, ipady=35)
num6 = Button(frame, text="6", command=lambda: fun("6"))
num6.grid(row=1, column=2, ipadx=35, ipady=35)
num7 = Button(frame, text="7", command=lambda: fun("7"))
num7.grid(row=0, column=0, ipadx=35, ipady=35)
num8 = Button(frame, text="8", command=lambda: fun("8"))
num8.grid(row=0, column=1, ipadx=35, ipady=35)
num9 = Button(frame, text="9", command=lambda: fun("9"))
num9.grid(row=0, column=2, ipadx=35, ipady=35)

plus = Button(frame, text="+", command=fun_plus)
plus.grid(row=0, column=4, ipadx=35, ipady=35)
equal = Button(frame, text="=", command=fun_equal)
equal.grid(row=3, column=2, ipadx=35, ipady=35)
minus = Button(frame, text="-", command=fun_minus)
minus.grid(row=2, column=4, ipadx=35, ipady=35)
multiplication = Button(frame, text="*", command=fun_multiply)
multiplication.grid(row=1, column=4, ipadx=35, ipady=35)
division = Button(frame, text="/", command=fun_divide)
division.grid(row=3, column=4, ipady=35, ipadx=35)

root.mainloop()
