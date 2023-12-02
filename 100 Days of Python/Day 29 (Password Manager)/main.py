import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    if len(password_entry.get()) > 0:
        password_entry.delete(0, tk.END)
    else:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for i in range(randint(8, 10))]
        password_symbols = [choice(symbols) for i in range(randint(2, 4))]
        password_numbers = [choice(numbers) for i in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers

        shuffle(password_list)

        password = "".join(password_list)
        password_entry.insert(0, password)
        pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    input_w = website_entry.get()
    input_u = user_entry.get()
    input_p = password_entry.get()
    new_data = {
        input_w:
            {"username": input_u, 
             "password": input_p
        }
    }

    if input_w == "" or input_p == "":
        messagebox.showerror(title="Error", message="Please enter a website and password")
    else:
        try:
            with open('data.json', 'r') as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
    
            with open('data.json', 'w') as data_file:
                #Saving the new data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            
# ---------------------------- FIND PASSWORD ------------------------------- # 
def find_password():
    input_w = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            username = data[input_w]["username"]
            password = data[input_w]["password"]
            if input_w in data.keys():
                messagebox.showinfo(title=input_w, message=f"Email: {username}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showerror(title="Error", message="No Data Found.")

# ---------------------------- UI SETUP ------------------------------- #
windows = tk.Tk()
windows.title("Password Generator")
windows.config(padx=50, pady=50, bg='white')

website_label = tk.Label(text="Website: ", bg='white')
website_label.grid(column=0, row=1)
user_label = tk.Label(text="Email/Username: ", bg='white')
user_label.grid(column=0, row=2)
password_label = tk.Label(text="Password: ", bg='white')
password_label.grid(column=0, row=3)


website_entry = tk.Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()
user_entry = tk.Entry(width=52)
user_entry.grid(column=1, row=2,columnspan= 2)
user_entry.insert(0, "kenaa@example.com")
password_entry = tk.Entry(width=33)
password_entry.grid(column=1, row=3)

search_button = tk.Button(text="Search: ", bg='white', width=17, command=find_password)
search_button.grid(column=2, row=1)

generator_button = tk.Button(text="Generate Password: ", bg='white', command=gen_password)
generator_button.grid(column=2, row=3)

add_button = tk.Button(text="Add: ", bg='white', width=51, command=save)
add_button.grid(column=1, row= 4, columnspan=2)


canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

windows.mainloop()