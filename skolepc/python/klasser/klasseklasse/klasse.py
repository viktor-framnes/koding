"""
Klasse som definerer en skoleklasse på Vgs.
"""
from Elev import *
class Klasse:
    def __init__(self,navn,laerer,rom) -> None:
        self.navn = navn
        self.rom = rom
        self.laerer = laerer
        self.elever = klasse3G
    def __str__(self) -> str:
        return f"{self.navn} i rom {self.rom}, med lærer {self.laerer} har elever {self.elever}"
    def bytt_rom(self,til_rom):
        self.rom = til_rom

klasse = Klasse("3G","Henrik","03-21")
legg_til("Viktor",2006)
for elev in klasse3G:
    print(elev)
