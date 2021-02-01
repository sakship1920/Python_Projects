from tkinter import *
from tkinter import messagebox  # have to import it cuz it is not Class
from random import shuffle, choice, randint
import pyperclip # using this we can directly paste password where we want to paste no need to copy
import json

# ---------------------------- SEARCH SITE ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} is added!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Fill Form", message="Please don't leave any field Empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \n Is it Okay to Save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Read the data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file, indent=4)

            else:
                # Update data
                data.update(new_data)
                # Save the data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)
                messagebox.askokcancel(title="Congrats", message="You have successfully entered tha data :)")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)
# Labels

website_lable = Label(text="Website:")
website_lable.grid(row=1, column=0)

email_lable = Label(text="Email/Username:")
email_lable.grid(row=2, column=0)

password_lable = Label(text="Password:")
password_lable.grid(row=3, column=0)

# Entries
website_entry = Entry(width=34 )
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sakship1920@gmail.com")  # This will already fill email entry
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
search_btn = Button(text="Search", width=14, command=find_password)
search_btn.grid(row=1, column=2)
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=44, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
