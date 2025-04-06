class Rektangel:
  """Klasse for å representere et rektangel"""
  def __init__(self, lengde, bredde):
    """Konstruktør"""
    self.lengde = lengde
    self.bredde = bredde
  
  def areal(self):
    """Metode for å beregne areal"""
    return self.lengde * self.bredde
  
  def visInfo(self):
    return f"Lengden: {self.lengde}, Bredde: {self.bredde} og Areal: {self.areal()}"

class Kvadrat(Rektangel):
  """Klasse for å representere et kvadrat"""
  def __init__(self, sidekant):
    super().__init__(sidekant, sidekant)

kvadrat1 = Kvadrat(2)
rektangel1 = Rektangel(2, 3)

print(kvadrat1.visInfo())
print(rektangel1.visInfo())