from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("CLOCK")
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
label=Label(root,font=("chiller",100),background="green",foreground="blue")
label.pack(anchor='center')
time()
mainloop()