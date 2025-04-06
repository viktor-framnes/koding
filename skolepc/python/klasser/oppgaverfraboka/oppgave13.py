class Billett():
  def __init__(self):
      self.mva = 0.12
      self.pris = 20

  def beregnPris(self):
    return self.pris + (self.pris * self.mva)

class Barnebillett(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.5
  
    def beregnPris(self):
        return super().beregnPris() * self.rabatt
  
class Vernepliktige(Billett):
    def __init__(self):
      super().__init__()
      self.rabatt = 0.1

    def beregnPris(self):
        return super().beregnPris() * 0.1
    
class Ukesbillett(Billett):
    def __init__(self):
       super().__init__()
       self.rabatt = 0.8

    def beregnPris(self):
       return super().beregnPris() * 7 * self.rabatt   

ukesbillett = Ukesbillett() 
billett1 = Vernepliktige()
print(billett1.beregnPris())
print(ukesbillett.beregnPris())