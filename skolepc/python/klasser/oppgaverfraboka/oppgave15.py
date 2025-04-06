from random import randint

class Terning:
    def __init__(self,antallSider) -> None:
        self.antallSider = antallSider

    def trillTerning(self):
            print(randint(1,self.antallSider))

class JukseTerning(Terning):
    def __init__(self, antallSider, antallKast) -> None:
        super().__init__(antallSider)
        self.antallKast = antallKast
    
    def trillTerning(self):
        Hoyestkast = 0
        for i in range(self.antallKast):
            kast = randint(1,self.antallSider)
            if kast > Hoyestkast:
                Hoyestkast = kast
        return Hoyestkast

terning1 = Terning(20)
terning1.trillTerning()

terning2 = JukseTerning(6,20)
print(terning2.trillTerning())