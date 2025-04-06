import tkinter as tk

class Sykdom():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1800x400")

    def tilstand0(self):
        boks = tk.Frame(self.window)
        boks.pack(expand=True,side="left")

        canvas = tk.Canvas(boks,bg="lightgrey",width=300,height=300)
        canvas.pack()

    def tilstand1(self):
        boks = tk.Frame(self.window)
        boks.pack(expand=True,side="left")

        canvas = tk.Canvas(boks,bg="#ff9696",width=300,height=300)
        canvas.pack()

        canvas.create_line(25,25,275,275,fill="black",width=10)

    def tilstand2(self):
        boks = tk.Frame(self.window)
        boks.pack(expand=True,side="left")

        canvas = tk.Canvas(boks,bg="red",width=300,height=300)
        canvas.pack()

        canvas.create_line(25,275,275,25,fill="white",width=10)

    def tilstand3(self):
        boks = tk.Frame(self.window)
        boks.pack(expand=True,side="left")

        canvas = tk.Canvas(boks,bg="#414141",width=300,height=300)
        canvas.pack()

        canvas.create_oval(140,140,160,160,fill="black")

    def tilstand4(self):
        boks = tk.Frame(self.window)
        boks.pack(expand=True,side="left")

        canvas = tk.Canvas(boks,bg="black",width=300,height=300)
        canvas.pack()

        canvas.create_oval(140,140,160,160,fill="white")

    def vis(self):
        self.window.mainloop()



syk1 = Sykdom()
syk1.tilstand0()
syk1.tilstand1()
syk1.tilstand2()
syk1.tilstand3()
syk1.tilstand4()
syk1.vis()