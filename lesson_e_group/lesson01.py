from tkinter import *
# ["txt", "file"]
from tkinter import ttk

window = Tk()


def enter():
    if password.get() == "123456789":
        VALUES = [
            "txt file",
            "py file",
            "html file",
            "js file",
            "docx file",
            "mp3 file",
            "png file",
            "exe file"
        ]
        text = """name
        
        
        
        directory
        
         
            file type        
        """

        def open_file():
            with open(f"{entry.get()}/{entry2.get()}.{choose.get().split()[0]}", "w") as file:
                file.close()

        root = Toplevel()
        root.title("file creator")
        root.geometry("550x350")
        label = LabelFrame(root, text="Actions")
        label.place(x=20, y=20, width=500, height=300)
        instruction = Label(label, text=text)
        instruction.place(x=0, y=0)
        entry = ttk.Entry(master=label)
        entry.pack(ipadx=100, ipady=5)
        Label(label).pack()
        entry2 = ttk.Entry(master=label)
        entry2.pack(ipadx=100, ipady=5)
        Label(label).pack()
        choose = ttk.Combobox(label, values=VALUES, width=45, height=50)
        choose.pack()
        Label(label).pack()
        submit = ttk.Button(master=label, text='Submit', command=open_file)
        submit.place(x=80, y=160)

        root.mainloop()


password = ttk.Entry()
password.pack()
button_enter = ttk.Button(text="enter", command=enter)
button_enter.pack()
window.mainloop()
