from tkinter import *
from tkinter import messagebox
import pyqrcode

a = Tk()
a.title("PythonGuides")
a.config(bg='#F25252')

def generate_QR():
    if len(user_input.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get())


lbl = Label(
    a,
    text="Enter message or URL",
    bg='#F25252'
    )
lbl.pack()

user_input = StringVar()
entry = Entry(
    a,
    textvariable = user_input
    )
entry.pack(padx=10)


button = Button(
    a,
    text = "generate_QR",
    width=15,
    command = generate_QR
    )
button.pack(pady=10)

img_lbl = Label(
    a,
    bg='#F25252')
img_lbl.pack()
output = Label(
    a,
    text="",
    bg='#F25252'
    )
output.pack()
 
a.mainloop()