from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("200x200")
    top.title("toplevel")
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()
    top.mainloop()
l = Label(root, text= "This is root window")
btn = Button(root, text= "Click here", command= topwin)
l.pack()
btn.pack()
root.mainloop()