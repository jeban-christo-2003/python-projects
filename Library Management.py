import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database initialization
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Create tables if not exist
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY, title TEXT, author TEXT, quantity INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS members
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, date_issued TEXT, date_returned TEXT, 
             FOREIGN KEY(book_id) REFERENCES books(id), FOREIGN KEY(member_id) REFERENCES members(id))''')

conn.commit()

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")

        # Create labels
        self.label_title = tk.Label(root, text="Title:")
        self.label_title.grid(row=0, column=0)

        self.label_author = tk.Label(root, text="Author:")
        self.label_author.grid(row=1, column=0)

        self.label_quantity = tk.Label(root, text="Quantity:")
        self.label_quantity.grid(row=2, column=0)

        # Create entry fields
        self.entry_title = tk.Entry(root)
        self.entry_title.grid(row=0, column=1)

        self.entry_author = tk.Entry(root)
        self.entry_author.grid(row=1, column=1)

        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.grid(row=2, column=1)

        # Create buttons
        self.button_add_book = tk.Button(root, text="Add Book", command=self.add_book)
        self.button_add_book.grid(row=3, column=0, columnspan=2)

        self.button_display_books = tk.Button(root, text="Display Books", command=self.display_books)
        self.button_display_books.grid(row=4, column=0, columnspan=2)

    def add_book(self):
        title = self.entry_title.get()
        author = self.entry_author.get()
        quantity = self.entry_quantity.get()

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number")
            return

        c.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)", (title, author, quantity))
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully")

    def display_books(self):
        display_window = tk.Toplevel()
        display_window.title("Books")

        # Create a listbox to display books
        listbox_books = tk.Listbox(display_window, width=50)
        listbox_books.pack()

        # Fetch books from the database and display
        c.execute("SELECT * FROM books")
        books = c.fetchall()
        for book in books:
            listbox_books.insert(tk.END, f"Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

root = tk.Tk()
app = LibraryManagementSystem(root)
root.mainloop()

# Close the database connection
conn.close()
