# Trenger å blande sammen Person- og populasjonsklassen#
# Vanskligste blir å lage en sammenheng mellom populasjonsarrayen og personen som skal være plassert på hver plass

from populasjon import Populasjon
from person import Person

#kjøre simulering:

dager, pop = map(int,input("Dager og populasjon...").split())

pop1 = Populasjon(pop)

for i in range(dager):
    pop1.tegnBrett()
    pop1.spredning()

personer = []
for i in range(pop):
    personer.append(Person()*pop)