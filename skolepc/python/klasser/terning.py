from random import randint

class Terning:
    def __init__(self,antallSider) -> None:
        self.antallSider = antallSider

    def trillTerning(self):
        for i in range(10):
            print(randint(1,self.antallSider))
        

terning1 = Terning(20)

terning1.trillTerning()