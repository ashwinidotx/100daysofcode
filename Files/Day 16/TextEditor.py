from Tkinter import *
from tkFileDialog import *
import tkMessageBox

filename= "untitled"

def newFile():
    global filename
    filename="Untitled File"
    text.delete(0.0,END)

def saveFile():
    global filename
    t = text.get(0.0,END)
    f = open(filename+'.txt','w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        tkMessageBox.showerror(title="Oops.!", message="File Not Saved. Please Try again...")

def openFile():
    global filename
    f = askopenfile(mode='r')
    filename = f.name
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)


root=Tk()
root.title("OS(ama) Text Editor")
root.minsize(width=300,height=150)
root.maxsize(width=700,height=350)

text=Text(root, width=700,height=350)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As...",command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()
