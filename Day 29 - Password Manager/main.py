import tkinter
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

password_char = [password_list.append(random.choice(letters)) for i in range(nr_letters)]

password_sym = [password_list.append(random.choice(symbols)) for i in range(nr_symbols)]

password_num = [password_list.append(random.choice(numbers)) for i in range(nr_numbers)]

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    webiste_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    if len(webiste_data) < 1 or len(email_data) < 1 or len(password_data) < 1:
        messagebox.showerror(title="Error", message="Don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=webiste_data, message=f"The entered details are:\nEmail: {email_data}\n"
                                                                 f"Password: {password_data}\nClick Ok to save")
        if is_ok:
            with open('data.txt', mode='a') as file:
                file.write(f"{webiste_data} | {email_data} | {password_data} \n")
            website_entry.delete(0, 50)
            password_entry.delete(0, 50)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0)
website_label.config(pady=10)

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
email_label.config(pady=10)

password_label = tkinter.Label(text="Password: ")
password_label.grid(row=3, column=0)
password_label.config(pady=10)

empty_label = tkinter.Label(text="")
empty_label.grid(row=4, column=0)
empty_label.config(pady=10)

website_entry = tkinter.Entry(width=41)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "guntasrikanth@gmail.com")

password_entry = tkinter.Entry(width=22)
password_entry.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generator Password", width=15)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
