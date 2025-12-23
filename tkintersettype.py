from tkinter import *

window = Tk()
window.title("Simple Tkinter GUI")
window.geometry("300x200")

Label(window, text="num" ,anchor="w", width=5).grid(column=0, row=0)

num = Entry(window, width=20)
num.grid(column=1, row=0)

res = Label(window, text="Result", anchor="w", width=20)
res.grid(column=1, row=3)

settype = IntVar()
settype.set(1)# default choice
Radiobutton(window, text="Binary", variable=settype, value=1).grid(column=0, row=4)
Radiobutton(window, text="Octal", variable=settype, value=2).grid(column=1, row=4)
Radiobutton(window, text="Hexadecimal", variable=settype, value=3).grid(column=0, row=5)
Radiobutton(window, text="Decimal", variable=settype, value=4).grid(column=1, row=5)
Button(window, text="Convert", command=lambda: [binary() if settype.get() == 1 else octal() if settype.get() == 2 else hexa() if settype.get() == 3 else decimal()], width=10).grid(column=1, row=6)

def binary():
    a = int(num.get())
    result = bin(a)
    res.config(text=str(result))
def octal():
    a = int(num.get())
    result = oct(a)
    res.config(text=str(result))
def hexa():
    a = int(num.get())
    result = hex(a)
    res.config(text=str(result))
def decimal():
    a = int(num.get())
    result = str(a)
    res.config(text=str(result))



window.mainloop()