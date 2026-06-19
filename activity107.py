import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        si = (principal * rate * time) / 100
        amount = principal * (1 + rate / 100) ** time
        ci = amount - principal
        result_label.config(text=f"Simple Interest = ₹{si:.2f}\n" f"Compound Interest = ₹{ci:.2f}\n" f"Final Amount = ₹{amount:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input","Please enter valid numeric values.")
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")
heading = tk.Label(root, text="Simple & Compound Interest Calculator",font=("Arial", 14, "bold"))
heading.pack(pady=10)
tk.Label(root, text="Principal Amount").pack()
principal_entry = tk.Entry(root, width=25)
principal_entry.pack()
tk.Label(root, text="Rate of Interest (%)").pack()
rate_entry = tk.Entry(root, width=25)
rate_entry.pack()
tk.Label(root, text="Time Period (Years)").pack()
time_entry = tk.Entry(root, width=25)
time_entry.pack()
calc_button = tk.Button(root, text="Calculate",command=calculate)
calc_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)
root.mainloop()