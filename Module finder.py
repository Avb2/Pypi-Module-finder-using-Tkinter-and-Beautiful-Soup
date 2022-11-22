from tkinter import *
from bs4 import BeautifulSoup
import requests
import pyperclip as pc

# Initiate tkinter
root = Tk()

# The search box where the user can input the module they are looking for
SearchBox = Entry(root)
SearchBox.grid(row=0, column=1)


# This is the function that will be initiated when the enter button is clicked
def SearchIt():  # sourcery skip: hoist-statement-from-if
    url = 'https://pypi.org/project/'
    # User search
    search = SearchBox.get()
    url += search

    # Run requests and scrapes for the pip command
    req = requests.get(url)
    result = BeautifulSoup(req.text, 'html.parser')
    try:
        pip_command = result.find('span', {'id': 'pip-command'})
        found = pip_command.text
        print(found)
        # If command is found, it will be displayed
        display = Label(root, text=found)
        display.grid(row=1, column=1)

        # Adds the pip command to clipboard
        pc.copy(found)
# If the user search can't be found
    except Exception:
        cant_find = 'Sorry I couldnt find that.'
        print(cant_find)
        display = Label(root, text=cant_find)
        display.grid(row=1, column=1)

# Clears the label that displays the pip command
def clear_text():
    display = Label(root, text='            ')
    display.grid(row=1, column=1)


# Enter button
Enter = Button(root, text='enter', command=lambda: SearchIt())
Enter.grid(row=0, column=0)

# Display documentation to user
display = Label(root, text='')
display.grid(row=1, column=1)

# Clear button
Clear = Button(text='clear', command=lambda: clear_text())
Clear.grid(row=1, column=0)

# Run loop
root.mainloop()
