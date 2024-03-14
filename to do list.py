import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")
        
        self.tasks = []
        self.categories = ["Personal", "Work", "Study", "Shopping"]
        self.selected_category = tk.StringVar(value=self.categories[0])
        
        self.create_widgets()
        
    def create_widgets(self):
        # Category Selection
        category_frame = tk.Frame(self.master)
        category_frame.pack(pady=10)
        
        category_label = tk.Label(category_frame, text="Select Category:")
        category_label.grid(row=0, column=0, padx=(10, 5))
        
        category_menu = tk.OptionMenu(category_frame, self.selected_category, *self.categories)
        category_menu.grid(row=0, column=1, padx=(5, 10))
        
        # Task Entry
        task_entry_frame = tk.Frame(self.master)
        task_entry_frame.pack(pady=5)
        
        self.task_entry = tk.Entry(task_entry_frame, width=50)
        self.task_entry.grid(row=0, column=0, padx=10)
        self.task_entry.focus_set()
        
        add_button = tk.Button(task_entry_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5)
        
        # Task List
        self.task_list = tk.Listbox(self.master, width=60, height=15)
        self.task_list.pack(pady=10)
        
        # Button Frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=5)
        
        complete_button = tk.Button(button_frame, text="Mark Complete", command=self.mark_complete)
        complete_button.grid(row=0, column=0, padx=5)
        
        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=0, column=1, padx=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, self.selected_category.get()))
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task, category in self.tasks:
            self.task_list.insert(tk.END, f"[{category}] {task}")
    
    def mark_complete(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            task, category = self.tasks.pop(index)
            self.tasks.insert(index, (f"{task} (Completed)", category))
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task.")
    
    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
