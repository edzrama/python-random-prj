from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

default_email = None

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    global default_email
    website = input_web.get()
    email: str = input_user.get()
    password = input_password.get()
    if website == "" or not email or password == "":
        messagebox.showerror(title="Cannot be blank", message="Please don't leave any fields empty")
    else:
        new_data = {
            website: {
                "email": email,
                "password": password
            }}
        # record = f"{website} | {email} | {input_password.get()}"
        if is_ok := messagebox.askokcancel(title="Save record to file", message="Are you sure you want to save this " "information?"):
            try:
                with open("records.json", mode="r") as json_file:
                    data = json.load(json_file)
            except (FileNotFoundError, ValueError):
                with open("records.json", mode="w") as json_file:
                    json.dump(new_data, json_file, indent=4)
            else:
                data.update(new_data)
                with open("records.json", mode="w") as json_file:
                    json.dump(data, json_file, indent=4)
            finally:
                messagebox.showinfo("showinfo", "Record Saved!")
                input_web.delete(0, END)
                # input_user.delete(0, END)
                input_password.delete(0, END)

            set_default = False
            if default_email != email:
                set_default = messagebox.askokcancel(title="Save User/Email", message="Do you wish to save this new"
                                                                                      " User/Email as default?")
            elif default_email == "":
                set_default = messagebox.askokcancel(title="Save User/Email", message="Do you wish to save "
                                                                                      "User/Email as default?")
            if set_default:
                with open("default.txt", mode="w") as default_file:
                    default_email = email
                    default_file.write(default_email)


def get_default_email():
    global default_email
    try:
        with open("default.txt", mode="r") as default_file:
            default_email = default_file.read()
            input_user.insert(END, default_email)
    except (FileNotFoundError, ValueError):
        input_user.insert(END, "")


def search():
    website = input_web.get()
    try:
        with open("records.json", mode="r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print("No record found!")
    except ValueError:
        with open("records.json", mode="w") as json_file:
            print("No record found!")
    else:
        try:
            record = data[website]
        except KeyError:
            messagebox.showerror(website, f"Record for {website} not found!")
        else:
            messagebox.showinfo(website, f"Email: {record['email']}\nPassword: {record['password']}")
            pyperclip.copy(record['password'])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=170, height=170)
canvas.create_image(85, 85, image=image)
canvas.grid(column=1, row=0, columnspan=2, sticky='w')

label_web = Label(text="Website: ")
label_web.grid(column=0, row=1, sticky='w')

label_user = Label(text="Email/Username: ")
label_user.grid(column=0, row=2, sticky='we')

label_password = Label(text="Password: ")
label_password.grid(column=0, row=3, sticky='w')

input_web = Entry(width=22)
input_web.grid(column=1, row=1, columnspan=2, sticky='w')
input_web.focus()

input_user = Entry(width=40)
input_user.grid(column=1, row=2, columnspan=2, sticky='w')
input_user.insert(0, "")

input_password = Entry(width=22)
input_password.grid(column=1, row=3, sticky='w')

button_password = Button(text="Generate Password", command=generate_password)
button_password.grid(column=2, row=3, sticky='we')

button_add = Button(text="Add", command=save_to_file)
button_add.grid(column=1, row=4, columnspan=2, sticky='we')

button_search = Button(text="Search", command=search)
button_search.grid(column=2, row=1, sticky='we')
get_default_email()
window.mainloop()
