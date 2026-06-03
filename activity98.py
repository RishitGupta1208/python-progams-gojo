from tkinter import *
root = Tk()
root.title('product generator')
root.geometry('400x300')
lbl = Label(text="Enter multiplicand", fg="white", bg="#3E436F")
entry = Entry()
lbl2 = Label(text="Enter multiplier", fg="white", bg="#3E436F")
entry2 = Entry()
def display():
    try:
        no1 = int(entry.get())
        no2 = int(entry2.get())
        answer = no1 * no2
        text_box.delete("1.0", END)
        text_box.insert(END, f"Answer is {answer}")
    except ValueError:
        text_box.delete("1.0", END)
        text_box.insert(END, "Please enter valid numbers")
text_box = Text(height=3)
btn = Button(text="Begin",command=display,height=1,bg="#1261A0",fg="white")
lbl.pack()
entry.pack()
lbl2.pack()
entry2.pack()
btn.pack()
text_box.pack()
root.mainloop()