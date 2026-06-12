from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry('100x100')
countv=0
def count():
    global countv
    countv+=1
    print("\n",countv)
button=Button(text="click me",command=count)
button.pack()
window.mainloop()