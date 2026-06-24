from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title('Cash COunter')
root.geometry('600x700')
root.configure('light blue')
upload=Image.open('OIP (1).jpg')
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,bg="light blue")
label.place(x=180,y=20)
label1=Label(root,text='Hey user!Welcome to the denomination calculation appliccation',
            bg="light blue" )
label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    msgbox=messagebox.showinfo('Alert','do you want to continue taking the denomination count')
    if msgbox=="ok":
        topwin()
Btn=Button(root,text='Lets get started',command=msg,bg="brown",fg='white')
Btn.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.title('denominator calculator')
    top.geometry('600x700')
    top.configure(bg="light grey")
    label=Label(top,text='Enter total amount',bg="light grey")
    entry=Entry(top)
    lbl=Label(top,text='Here are the notes for each denomination',bg="light grey")
    l1=Label(top,text="2000",bg="light grey")
    l2=Label(top,text="500",bg="light grey")
    l3=Label(top,text="100",bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculator():
        try:
            amount=int(entry.get())
            note