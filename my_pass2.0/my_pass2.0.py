from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import os
import sys
import json

def resource_path(relative_path):
    """ Get absolute path to resource """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def search():
    """Searches data.json for info in given web entry"""
    web = web_entry.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            found_data = data[web]
    except KeyError:
        messagebox.showinfo(title="Oops", message=f"No entry found for {web}!")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Data file not found! You may not have created a file yet")
    else:
        messagebox.showinfo(title=web, message=f"Username: {found_data['username']}\nPassword: {found_data['password']}")

def gen_pwd():
    """ Generates a random password and copies to users clipboard"""
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', 
    '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']
    rand_chars = random.choices(chars, k= 14)
    pwd = [char for char in rand_chars]
    new_pwd = ''.join(pwd)
    pwd_entry.insert(0, new_pwd)
    pyperclip.copy(new_pwd)

def save():
    """ Saves user input to data.json """
    web = web_entry.get()
    user = email_entry.get()
    pwd = pwd_entry.get()
    new_data = {
        web: {
            "username": user,
            "password": pwd,
        }
    }
    if len(web) == 0 or len(user) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pwd_entry.delete(0, END)

# window layout
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# Background
canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file=resource_path("logo.png"))
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)
# Labels
web_text = Label(text="Website:")
web_text.grid(row=1, column=0, sticky='e')
email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)
pswd_text = Label(text="Password:")
pswd_text.grid(row=3, column=0, sticky='e')
# Buttons
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky='we')
gen_button = Button(text="Generate Password", command=gen_pwd)
gen_button.grid(row=3, column=2, sticky='w')
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='we')
# Entries
web_entry = Entry()
web_entry.grid(row=1, column=1, sticky='we')
web_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky='we')
pwd_entry = Entry()
pwd_entry.grid(row=3, column=1, sticky='we')

window.mainloop()