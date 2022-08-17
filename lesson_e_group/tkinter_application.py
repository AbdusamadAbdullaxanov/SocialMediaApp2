from tkinter import *
import os

root = Tk()
name = Entry()
name.pack(side=TOP)


def execute():
    with open(f"{name.get()}.py", "w") as file:
        file.write(text.get('1.0', END))
        file.close()
    os.system(f'cmd /c "python -m {name.get()}.py"')


text = Text()
text.pack(side=RIGHT)
button = Button(text="run", command=execute)
button.pack(side=LEFT)
mainloop()
