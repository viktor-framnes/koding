import tkinter as tk
import time

class Test(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(200,200)
        self.canvas = tk.Canvas(self,bg="blue",width=100,height=100)
        self.canvas.pack(expand=True)
        tk.Button(self, text="Start", command=lambda: kjor(self)).pack(side="bottom")


def kjor(self):
    farger = ["red","yellow","black","purple","green","blue","lightblue","pink"]
    for i in range(8):
        x.canvas.configure(bg=farger[i])
        x.canvas.update()
        time.sleep(1)

x = Test()
x.mainloop()