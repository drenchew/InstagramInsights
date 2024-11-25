import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from insta import InstagramInsights
import os


def open_file():
    os.startfile('unfollowers.txt')

def show_file():

    open_button = tk.Button(root, text="Open", command=open_file)
    open_button.place.pack()
    tk.Label(root, text="Ready! Check the unfollowers.txt file.", bg="cyan").place(x=50, y=160)


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        try:
            instagram = InstagramInsights(username, password)
            instagram.get_unfollowers(username, save=True)
            show_file()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter both username and password.")

def background():
    background_image = Image.open("bg.png")  
    background_image = background_image.resize((300, 200))
    bg_photo = ImageTk.PhotoImage(background_image)

    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

root = tk.Tk()
root.title("Instagram Insights")
root.geometry("300x200")

background()  

username_label = tk.Label(root, text="Username:", bg="cyan") 
username_label.place(x=50, y=50)
username_entry = tk.Entry(root)
username_entry.place(x=120, y=50)

password_label = tk.Label(root, text="Password:", bg="cyan")
password_label.place(x=50, y=90)
password_entry = tk.Entry(root, show="*")
password_entry.place(x=120, y=90)

login_button = tk.Button(root, text="Login", command=login)
login_button.place(x=120, y=130)

root.mainloop()
