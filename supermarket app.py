import tkinter as tk
from tkinter import messagebox

class SupermarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Billing App")

        self.items = {"Apple": 10, "Banana": 5, "Orange": 8, "Mango": 12}  # Sample items with prices
        self.cart = {}
        self.total_price = tk.DoubleVar(value=0)

        # Create labels and entry widgets
        tk.Label(root, text="Select Item:").grid(row=0, column=0, padx=10, pady=5)
        self.item_var = tk.StringVar(root)
        self.item_var.set("Apple")  # Default item
        self.item_option = tk.OptionMenu(root, self.item_var, *self.items.keys())
        self.item_option.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(root, text="Add to Cart", command=self.add_to_cart).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        tk.Label(root, text="Cart:").grid(row=3, column=0, padx=10, pady=5)
        self.cart_text = tk.Text(root, height=10, width=30)
        self.cart_text.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Total Price:").grid(row=4, column=0, padx=10, pady=5)
        tk.Label(root, textvariable=self.total_price).grid(row=4, column=1, padx=10, pady=5)

        tk.Button(root, text="Generate Bill", command=self.generate_bill).grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def add_to_cart(self):
        item = self.item_var.get()
        quantity = int(self.quantity_entry.get())

        if item in self.items:
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity

            self.update_cart_text()
            self.calculate_total_price()
        else:
            messagebox.showerror("Error", "Invalid item selected.")

    def update_cart_text(self):
        self.cart_text.delete('1.0', tk.END)
        for item, quantity in self.cart.items():
            self.cart_text.insert(tk.END, f"{item}: {quantity}\n")

    def calculate_total_price(self):
        total = sum(self.items[item] * quantity for item, quantity in self.cart.items())
        self.total_price.set(total)

    def generate_bill(self):
        if not self.cart:
            messagebox.showwarning("Warning", "Cart is empty.")
        else:
            bill = "\n".join([f"{item}: {quantity} x {self.items[item]} = {quantity * self.items[item]}" for item, quantity in self.cart.items()])
            bill += f"\n\nTotal Price: {self.total_price.get()}"
            messagebox.showinfo("Bill", bill)

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketApp(root)
    root.mainloop()

