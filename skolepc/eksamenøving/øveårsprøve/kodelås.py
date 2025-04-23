import tkinter as tk

class kodelos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(400,400)
        self.knapper = tk.Frame(self).pack()
        tk.Button(self.knapper,text="1",command=lambda:self.trykk(1)).grid(row=1,column=1)

    def trykk(self,a):
        print(a)

_ = kodelos()
_.mainloop()