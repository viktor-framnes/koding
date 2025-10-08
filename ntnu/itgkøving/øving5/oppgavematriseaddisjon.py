import random


class Random_matrise():
    def __init__(self,b=0,h=0):
        self.matrise = [[random.randint(0,9) for i in range(b)] for j in range(h)]
        self.h = h
        self.b = b

    def print_matrise(self,x):
        print(f"{x}=[")
        for rad in self.matrise:
            print(f"    {rad}")
        print("  ]")

def matrise_addisjon(x1,x2):
    if x1.b != x2.b or x1.h != x2.h:
        print("Matrisene er ikke av samme dimensjon")
    else:
        C=[]
        for i in range(x1.h):
            temp = []
            for j in range(x1.b):
                temp.append(x1.matrise[i][j]+x2.matrise[i][j])
            C.append(temp)


        x3 = Random_matrise()
        x3.matrise = C
        return x3.print_matrise("C")

x1 = Random_matrise(3,4)
x1.print_matrise("A")
x2 = Random_matrise(3,4)
x2.print_matrise("B")
matrise_addisjon(x1,x2)