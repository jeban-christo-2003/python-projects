import tkinter as tk
from tkinter import messagebox

class RecipeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe Sharing Platform")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label_title = tk.Label(self.frame, text="Title:")
        self.label_title.grid(row=0, column=0)
        self.entry_title = tk.Entry(self.frame)
        self.entry_title.grid(row=0, column=1)

        self.label_ingredients = tk.Label(self.frame, text="Ingredients:")
        self.label_ingredients.grid(row=1, column=0)
        self.entry_ingredients = tk.Text(self.frame, width=30, height=5)
        self.entry_ingredients.grid(row=1, column=1)

        self.label_instructions = tk.Label(self.frame, text="Instructions:")
        self.label_instructions.grid(row=2, column=0)
        self.entry_instructions = tk.Text(self.frame, width=30, height=5)
        self.entry_instructions.grid(row=2, column=1)

        self.button_submit = tk.Button(self.frame, text="Submit", command=self.submit_recipe)
        self.button_submit.grid(row=3, columnspan=2)

    def submit_recipe(self):
        title = self.entry_title.get()
        ingredients = self.entry_ingredients.get("1.0", tk.END)
        instructions = self.entry_instructions.get("1.0", tk.END)
        # Here you can implement the logic to save the recipe data
        messagebox.showinfo("Success", "Recipe submitted successfully!")

def main():
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
