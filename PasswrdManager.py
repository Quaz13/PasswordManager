import tkinter as tk  # Import the tkinter library for GUI development
from tkinter import messagebox  # Import messagebox for displaying messages to the user
import json  # Import json for handling the storage and retrieval of passwords
import os  # Import os to check the existence of files

# Define the filename where passwords will be stored
PASSWORD_FILE = "passwords.json"

# Check if the password file exists; if not, create it
if not os.path.exists(PASSWORD_FILE):
    with open(PASSWORD_FILE, 'w') as file:
        # Initialize the file with an empty dictionary
        json.dump({}, file)

# Function to save the password for a website
def save_password():
    # Get the website, username, and password entered by the user
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Check if any of the fields are empty
    if not website or not username or not password:
        # Show an error message if any field is empty
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    # Create a dictionary to store the new data
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    try:
        # Try to open the password file and load existing data
        with open(PASSWORD_FILE, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        # If the file is empty or corrupted, start with an empty dictionary
        data = {}

    # Update the existing data with the new entry
    data.update(new_data)

    # Write the updated data back to the file
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(data, file, indent=4)  # Indent for readability

    # Clear the input fields after saving the password
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    # Show a success message to the user
    messagebox.showinfo("Success", f"Password saved for {website}")

# Function to search for a saved password
def search_password():
    # Get the website entered by the user
    website = website_entry.get()

    # Check if the website field is empty
    if not website:
        # Show an error message if the website field is empty
        messagebox.showerror("Error", "Please enter the website name!")
        return

    try:
        # Try to open the password file and load the data
        with open(PASSWORD_FILE, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        # If the file is empty or corrupted, show an error message
        messagebox.showerror("Error", "No passwords found!")
        return

    # Check if the website exists in the stored data
    if website in data:
        # Retrieve the username and password for the website
        username = data[website]["username"]
        password = data[website]["password"]
        # Show the found details to the user
        messagebox.showinfo("Password Found", f"Website: {website}\nUsername: {username}\nPassword: {password}")
    else:
        # Show an error message if no details are found for the website
        messagebox.showerror("Error", "No details found for this website!")

# GUI Setup
root = tk.Tk()  # Create the main window
root.title("Password Manager")  # Set the window title

# Website Label and Entry
tk.Label(root, text="Website:").grid(row=0, column=0, padx=10, pady=10)  # Label for the website field
website_entry = tk.Entry(root, width=35)  # Entry field for the website
website_entry.grid(row=0, column=1, padx=10, pady=10)  # Position the entry field

# Username Label and Entry
tk.Label(root, text="Username/Email:").grid(row=1, column=0, padx=10, pady=10)  # Label for the username/email field
username_entry = tk.Entry(root, width=35)  # Entry field for the username/email
username_entry.grid(row=1, column=1, padx=10, pady=10)  # Position the entry field

# Password Label and Entry
tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=10)  # Label for the password field
password_entry = tk.Entry(root, width=35, show="*")  # Entry field for the password with masking
password_entry.grid(row=2, column=1, padx=10, pady=10)  # Position the entry field

# Save Button
save_button = tk.Button(root, text="Save Password", command=save_password)  # Button to save the password
save_button.grid(row=3, column=1, pady=10)  # Position the save button

# Search Button
search_button = tk.Button(root, text="Search Password", command=search_password)  # Button to search for a password
search_button.grid(row=4, column=1, pady=10)  # Position the search button

# Start the GUI loop to display the window and wait for user interaction
root.mainloop()

