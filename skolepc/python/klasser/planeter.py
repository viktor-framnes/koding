import math as m


class Planeter:
    """
    Klasse for å lage planet-objekter.

    Parametre:
        navn (str): Planetens navn
        solavstand (float): Avstand fra sola i millioner km
        radius (float): Planetens radius i km
        antallRinger = 0 (int): Antall ringer rundt planeten
    """
    def __init__(self,navn,solavstand,radius,antallRinger = 0) -> None:
        """
        Konstruktør
        """
        self.navn = navn
        self.solavstand = solavstand # i milliioner km
        self.radius = radius
        self.antallRinger = antallRinger
        
    def volum(self):
        return (4/3) * m.pi * self.radius**3
    
    def overflate(self):
        return 4 * m.pi * self.radius**2
    
    def lyshastighets(self):
        return (self.solavstand*1000000/300000)/60
    
    def visInfo(self):
        print(f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")

    
merkur = Planeter("merkur",57.91,2439.7)
venus = Planeter("venus",108.2,6051.8)
jorda = Planeter("jorda",149.6,6371)
mars = Planeter("mars",3389.5,227.9)
jupiter = Planeter("jupiter",69911,778.5)
saturn = Planeter("saturn",58232,1434000)
uranus = Planeter("uranus",25362,2871000)
neptun = Planeter("neptun",24622,4495000)
pluto = Planeter("pluto",2,4,1)

print(f"{merkur.volum():.2f}")
print(f"{venus.volum():.2f}")
print(f"{jorda.volum():.2f}")
print(f"{mars.volum():.2f}")
print(f"{jupiter.volum():.2f}")
print(saturn.volum())
print(uranus.volum())
print(neptun.volum())
print(f"{jorda.lyshastighets():.1f}")