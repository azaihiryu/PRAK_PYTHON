from tkinter import *

window = Tk()
window.title("Simple Tkinter GUI")
window.geometry("300x200")

Label(window, text="x" ,anchor="w", width=5).grid(column=0, row=0)
Label(window, text="y" ,anchor="w", width=5).grid(column=0, row=1)

x = Entry(window, width=20)
x.grid(column=1, row=0)
y = Entry(window, width=20)
y.grid(column=1, row=1)

res = Label(window, text="Result", anchor="w", width=20)
res.grid(column=1, row=3)

#FUNCTION
def add():
    a = int(x.get())
    b = int(y.get())
    result = a + b
    res.config(text=str(result))
def subtract():
    a = int(x.get())
    b = int(y.get())
    result = a - b
    res.config(text=str(result))
def multiply():
    a = int(x.get())
    b = int(y.get())
    result = a * b
    res.config(text=str(result))
def divide():
    a = int(x.get())
    b = int(y.get())
    if b != 0:
        result = a / b
        res.config(text=str(result))
    else:
        res.config(text="Error: Div by 0")
def modulus():
    a = int(x.get())
    b = int(y.get())
    result = a % b
    res.config(text=str(result))
    
#BUTTON

Button(window, text="+", command=add, width=5).grid(column=0, row=4)
Button(window, text="-", command=subtract, width=5).grid(column=1, row=4)
Button(window, text="*", command=multiply, width=5).grid(column=0, row=5)
Button(window, text="/", command=divide, width=5).grid(column=1, row=5)
Button(window, text="%", command=modulus, width=5).grid(column=0, row=6)
Button(window, text="Exit", command=window.quit, width=5).grid(column=1, row=6)

window.mainloop()