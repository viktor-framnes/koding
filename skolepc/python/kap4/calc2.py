import tkinter as tk

window = tk.Tk(className="Kalkulator")
bredde = 300
hoyde = 450
window.minsize(bredde,hoyde)

header = tk.Frame(window)
header.configure(
    background="palevioletred",
    height=80,
    width=bredde
)
header.pack_propagate(False)
header.pack(fill="x")

mid = tk.Frame(window)
mid.configure(
    background="lightpink",
    height=350,
    width=bredde
)
mid.pack(fill="both", expand=True, side="right")

knappframe = tk.Frame(mid, background="lightpink")
knappframe.pack(expand=True)


l1 = tk.Label(header)
l1.configure(
    foreground="black",
    background="white",
    width=38,
    height=3,
    font=("Helvetica", 9, "bold"),
    anchor="e"
)
l1.pack(expand=True)

b2 = tk.Button(knappframe,text=2,font=100,width=6,height=3)
b1 = tk.Button(knappframe,text=1,font=100,width=6,height=3)
b3 = tk.Button(knappframe,text=3,font=100,width=6,height=3)
b4 = tk.Button(knappframe,text=4,font=100,width=6,height=3)
b5 = tk.Button(knappframe,text=5,font=100,width=6,height=3)
b6 = tk.Button(knappframe,text=6,font=100,width=6,height=3)
b7 = tk.Button(knappframe,text=7,font=100,width=6,height=3)
b8 = tk.Button(knappframe,text=8,font=100,width=6,height=3)
b9 = tk.Button(knappframe,text=9,font=100,width=6,height=3)
b0 = tk.Button(knappframe,text=0,font=100,width=6,height=3)
deleknapp = tk.Button(knappframe,text="/",font=100,width=6,height=3)
gangeknapp = tk.Button(knappframe,text="*",font=100,width=6,height=3)
minusknapp = tk.Button(knappframe,text="-",font=100,width=6,height=3)
plussknapp = tk.Button(knappframe,text="+",font=100,width=6,height=3)
likknapp = tk.Button(knappframe,text="=",font=100,width=6,height=3)
fortegnknapp = tk.Button(knappframe,text="+/-",font=100,width=6,height=3)
kommaknapp = tk.Button(knappframe,text=",",font=100,width=6,height=3)
cknapp = tk.Button(knappframe,text="C",font=100,width=6,height=3)
ceknapp = tk.Button(knappframe,text="CE",font=100,width=6,height=3)
hevetknapp = tk.Button(knappframe,text="x^^2",font=100,width=6,height=3)

b9.grid(row=1,column=2)
b8.grid(row=1,column=1)
b7.grid(row=1,column=0)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b0.grid(row=4,column=1)
deleknapp.grid(column=3,row=0)
gangeknapp.grid(column=3,row=1)
minusknapp.grid(column=3,row=2)
plussknapp.grid(column=3,row=3)
likknapp.grid(column=3,row=4)
fortegnknapp.grid(column=0,row=4)
kommaknapp.grid(column=2,row=4)
cknapp.grid(column=2,row=0)
ceknapp.grid(column=1,row=0)
hevetknapp.grid(column=0,row=0)

def k1(e):
    l1["text"] += "1"

b1.bind("<Button-1>",k1)
def k2(e):
    l1["text"] += "2"

b2.bind("<Button-1>",k2)
def k3(e):
    l1["text"] += "3"

b3.bind("<Button-1>",k3)
def k4(e):
    l1["text"] += "4"

b4.bind("<Button-1>",k4)
def k5(e):
    l1["text"] += "5"

b5.bind("<Button-1>",k5)
def k6(e):
    l1["text"] += "6"

b6.bind("<Button-1>",k6)
def k7(e):
    l1["text"] += "7"

b7.bind("<Button-1>",k7)
def k8(e):
    l1["text"] += "8"

b8.bind("<Button-1>",k8)
def k9(e):
    l1["text"] += "9"

b9.bind("<Button-1>",k9)
def k0(e):
    l1["text"] += "0"

b0.bind("<Button-1>",k0)

tall1 = 0
valg = ""

def dele(e):
    global valg
    global tall1
    tall1 = float(l1["text"])
    valg = "dele"
    l1["text"] = ""

deleknapp.bind("<Button-1>",dele)

def gange(e):
    global valg
    global tall1
    tall1 = float(l1["text"])
    valg = "gange"
    l1["text"] = ""

gangeknapp.bind("<Button-1>",gange)

def minus(e):
    global valg
    global tall1
    tall1 = float(l1["text"])
    valg = "minus"
    l1["text"] = ""

minusknapp.bind("<Button-1>",minus)

def pluss(e):
    global valg
    global tall1
    tall1 = float(l1["text"])
    valg = "pluss"
    l1["text"] = ""

plussknapp.bind("<Button-1>",pluss)

def lik(e):
    global valg
    global tall1
    tall2 = float(l1["text"]) 
    if valg == "dele":
        l1["text"] = tall1 / tall2
    elif valg == "gange":
        l1["text"] = tall1 * tall2
    elif valg == "minus":
        l1["text"] = tall1 - tall2
    elif valg == "pluss":
        l1["text"] = tall1 + tall2

likknapp.bind("<Button-1>",lik)

def endrefortegn(e):
    x = float(l1["text"]) * -1
    l1["text"] = x
fortegnknapp.bind("<Button-1>",endrefortegn)

def komma(e):
    l1["text"] += "."

kommaknapp.bind("<Button-1>",komma)

def iandre(e):
    x = float(l1["text"])**2
    l1["text"] = x

hevetknapp.bind("<Button-1>",iandre)

def ce(e):
    l1["text"] = ""

ceknapp.bind("<Button-1>",ce)

def c(e):
    global tall1
    l1["text"] = ""
    tall1 = 0

cknapp.bind("<Button-1>",c)

window.mainloop()