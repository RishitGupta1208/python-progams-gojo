import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime
def calculate_age():
    try:
        birth_date = datetime.strptime(entry.get(), "%Y-%m-%d").date()
        today = date.today()
        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future!")
            return
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day
        if days < 0:
            months -= 1
            previous_month = today.month - 1 or 12
            if previous_month in [1, 3, 5, 7, 8, 10, 12]:
                days += 31
            elif previous_month in [4, 6, 9, 11]:
                days += 30
            else:
                if (today.year % 4 == 0 and today.year % 100 != 0) or (today.year % 400 == 0):
                    days += 29
                else:
                    days += 28
        if months < 0:
            years -= 1
            months += 12
        result_label.config(text=f"Age: {years} Years, {months} Months, {days} Days")
    except ValueError:
        messagebox.showerror("Invalid Input","Enter date in YYYY-MM-DD format")
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x250")
title = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"))
title.pack(pady=10)
tk.Label(root, text="Enter Birth Date (YYYY-MM-DD):").pack()
entry = tk.Entry(root, width=20)
entry.pack(pady=5)
calc_btn = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)
root.mainloop()