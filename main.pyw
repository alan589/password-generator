#Password Generator Project
import random
from tkinter import *
from tkinter import messagebox
import pyperclip as pc

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = int(letter_spinbox.get())
    nr_symbols = int(symbol_spinbox.get())
    nr_numbers = int(number_spinbox.get())

    password_list = []

    is_checked = checked_state.get()
    if is_checked:
        password_list += random.sample(letters, k=nr_letters)
        password_list += random.sample(symbols, k=nr_symbols)
        password_list += random.sample(numbers, k=nr_numbers)
    else:

        password_list += random.choices(letters, k=nr_letters)
        password_list += random.choices(symbols, k=nr_symbols)
        password_list += random.choices(numbers, k=nr_numbers)

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

def copy_password():
    pc.copy(password_entry.get())
    messagebox.showinfo(title="Password", message="Copied! :)")

FONT = ("Arial", 10, "bold")
PRIMARY_BG = "#C62300"

# UI
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=PRIMARY_BG)
window.resizable(False, False)


canvas = Canvas(width=128, height=128, bg=PRIMARY_BG, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(64, 64, image=logo_img)
canvas.grid(column=0, row=0, pady=30, columnspan=2)

# Labels

letter_label = Label(text="Letters:", bg=PRIMARY_BG, fg="white", font=FONT)
number_label = Label(text="Numbers:", bg=PRIMARY_BG, fg="white", font=FONT)
letter_label.grid(column=0,row=1, padx=60)
number_label.grid(column=0,row=2)

symbol_label = Label(text="Symbols:", bg=PRIMARY_BG, fg="white", font=FONT)
symbol_label.grid(column=0,row=3)

# Checkbuttons
checked_state = IntVar()
checkbutton = Checkbutton(text="No repeated characters", variable=checked_state,
                          bg=PRIMARY_BG, fg="white", font=FONT, selectcolor=PRIMARY_BG,
                          activeforeground="white", activebackground=PRIMARY_BG)
checked_state.get()
checkbutton.grid(column=0, row=4, columnspan=2)

# Entries
password_entry = Entry(width=25)
password_entry.grid(column=0, row=5, ipady=4)

# Spinboxes

letter_spinbox = Spinbox(from_=0, to=52, width=5, state="readonly")
letter_spinbox.grid(column=1, row=1, sticky="W")

number_spinbox = Spinbox(from_=0, to=10, width=5, state="readonly")
number_spinbox.grid(column=1, row=2, sticky="W")

symbol_spinbox = Spinbox(from_=0, to=9, width=5, state="readonly")
symbol_spinbox.grid(column=1, row=3, sticky="W")


# Buttons

generate_button = Button(text="Generate", font=FONT, cursor="hand2", command=generate_password, width=10)
generate_button.grid(column=1, row=5, pady=30)

copy_button = Button(text="Copy", font=FONT, cursor="hand2", width=15, command=copy_password)
copy_button.grid(column=0, row=6, columnspan=2)


window.mainloop()