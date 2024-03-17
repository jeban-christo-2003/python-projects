import random
import tkinter as tk
from tkinter import messagebox

def generate_otp():
    otp = random.randint(1000, 9999)
    otp_label.config(text=f"Generated OTP: {otp}")

def verify_otp():
    entered_otp = otp_entry.get()
    generated_otp = otp_label.cget("text").split(":")[1].strip()
    if entered_otp == generated_otp:
        messagebox.showinfo("Success", "OTP Verified Successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP!")

# Create the main window
window = tk.Tk()
window.title("OTP Generator")

# Create widgets
otp_label = tk.Label(window, text="Click 'Generate OTP' to get your OTP")
generate_button = tk.Button(window, text="Generate OTP", command=generate_otp)
otp_entry_label = tk.Label(window, text="Enter OTP:")
otp_entry = tk.Entry(window)
verify_button = tk.Button(window, text="Verify OTP", command=verify_otp)

# Place widgets in the window
otp_label.pack(pady=10)
generate_button.pack(pady=5)
otp_entry_label.pack(pady=5)
otp_entry.pack(pady=5)
verify_button.pack(pady=5)

# Run the application
window.mainloop()


