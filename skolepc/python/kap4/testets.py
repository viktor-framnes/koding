from tkinter import *

root = Tk()

b = Button(root, text="Delete me", command=lambda: b.pack_forget())
a = Button(root, text="make", command=lambda: b.pack())
b.pack()
a.pack()

root.mainloop()