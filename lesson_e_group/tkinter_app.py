from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesnocancel, showerror
import sqlite3

connection = sqlite3.connect("EncryptDatabase.db")
connection.cursor().execute(
    """
    CREATE TABLE IF NOT EXISTS "Base" (
    "id" INTEGER,
    "fullname" TEXT NOT NULL, "email"TEXT NOT NULL UNIQUE, "text_input" TEXT NOT NULL, PRIMARY KEY("id")
    );
    """
)
connection.commit()


def encrypt(word: str, hint: str):
    data = ""
    for i in word:
        if hint == "+":
            data += chr(ord(i) + 5)
        elif hint == "-":
            data += chr(ord(i) - 5)
    return data


root = Tk()
root.title("Encrypt Application")
root.config(bg="#B5BAB3")
root.resizable(False, False)
root.geometry("750x380")
LabelFrame(text="Forms").place(x=10, y=10, width=730, height=250)


# FUNCTIONS ____________________________________________________________________________________________________________
def insert_data():
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Base (fullname, email, text_input) VALUES (?, ?, ?)",
            (
                encrypt(fullname.get(), "+"), encrypt(email.get(), "+"),
                encrypt(main_input.get("1.0", END), "+")
            )
        )
        connection.commit()
    except Exception as error:
        showerror("Error", str(error))
    except sqlite3.IntegrityError as int_error:
        showerror("Database Error", str(int_error))
    else:
        showinfo("Success!", "Your request has been successfully inserted to database!!!")


def show_data():
    ask = askyesnocancel("Permission", "Do you want to extract data from encrypting?")
    try:
        cursor = connection.cursor()
        data = cursor.execute("""SELECT * FROM Base""")
        lst_of_data = data.fetchall()
        toplevel = Toplevel()
        toplevel.geometry("450x300")
        for j in lst_of_data:
            if ask:
                data = f"""fullname: {encrypt(word=j[1], hint='-')}\n
                email: {encrypt(word=j[2], hint='-')}\ntext: {encrypt(word=j[3], hint='-')}"""
            else:
                data = f"""fullname: {j[1]}\nemail: {j[2],}\ntext: {j[3]}"""
            Label(toplevel, text=data).pack()
        toplevel.mainloop()
    except sqlite3.IntegrityError as error:
        showerror("Exception", str(error))
    except ValueError:
        showerror("ValueError", "Nothing entered to reverse field!")


def delete_data():
    try:
        cursor = connection.cursor()
        try:
            fetch = cursor.execute("""SELECT id FROM Base WHERE id=(?)""", (id_to_delete.get(),)).fetchall()[0][0]
            cursor.execute("""DELETE FROM Base WHERE id=(?)""", (fetch,))
            connection.commit()
            showinfo("Success!", "Data has beem deleted successfully!!!")
        except IndexError:
            showerror("IdError", f"There is no data with id {id_to_delete.get()}")
    except Exception as error:
        showerror("Database error", str(error))


# END OF FUNCTIONS _____________________________________________________________________________________________________

form_frame = Frame(root)

form_frame.place(x=20, y=30, width=350)

Label(form_frame, text="Enter your fullname").pack()
fullname = ttk.Entry(form_frame)
fullname.pack(fill=X, ipady=6)
Label(form_frame).pack()

Label(form_frame, text="Now, enter your email").pack()
email = ttk.Entry(form_frame)
email.pack(fill=X, ipady=6)
Label(form_frame).pack()

Label(form_frame, text="Enter digit that we delete that digit id you entered").pack()
id_to_delete = ttk.Entry(form_frame)
id_to_delete.pack(fill=X, ipady=6)
Label(form_frame).pack()

text_frame = Frame(master=root)
text_frame.place(x=390, y=30, width=340, height=210)

Label(text_frame, text="Main Input").pack(fill=X)
main_input = Text(text_frame)
main_input.pack(fill=X)

button_frame = LabelFrame(root)
button_frame.config(bg="#B5BAB3")
button_frame.place(x=10, y=275, width=730, height=70)

btn_insert = Button(button_frame, text="INSERT", command=insert_data)
btn_insert.pack(side=LEFT, fill=Y, ipadx=70)

btn_insert = Button(button_frame, text="DELETE", command=delete_data)
btn_insert.pack(side=RIGHT, fill=Y, ipadx=70)

btn_show = Button(button_frame, text="SHOW DATA", command=show_data)
btn_show.pack(side=TOP, fill=Y, ipadx=70, ipady=70)

mainloop()
