from genericpath import exists
from msilib.schema import File
from tkinter import ttk
import tkinter
from PIL import  ImageTk, Image
import qrcode


root = tkinter.Tk()

root.geometry("500x500")
root.resizable(0,0)
root.title("QR Code Generator")

#Header
ttk.Label(root, text="QR Code Generator",font="arial 20 bold").pack()
#label 1
ttk.Label(root, text="Enter Link or Text:").place(x=50,y=100)
#text input
link = tkinter.StringVar()

ttk.Entry(root,width=50,textvariable=link).place(x=150,y=100)


def generate():
    image = qrcode.make(link.get())
    image.save("./Desktop/MyQr.jpg")
    path="./Desktop/MyQr.jpg"

        #QR display frame
    
    if exists(path):
        img = Image.open(path)
        photo = ImageTk.PhotoImage(img.resize((150, 150), Image.ANTIALIAS))
# Create a Label Widget to display the text or Image
        label = tkinter.Label(root, image = photo,width=150,height=150)
        label.place(x=180,y=250)    



ttk.Button(root,text="Generate",command=generate).place(x=220,y=150)


#exit button
ttk.Button(root,text="Exit",command=root.destroy).place(x=220,y=450)



root.mainloop()