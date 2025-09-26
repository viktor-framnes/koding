# generisk kode for plotting
# vi importerer pakkene vi trenger
import numpy as np
import matplotlib.pyplot as plt

a = -3/2
b = 11/2
c = -2

x = np.linspace(0,4,1000) # antall punkter i intervallet (0,1)
y = a*x**2+b*x+c # legg merke til at x^2 skrives som x**2
plt.plot(x, y) # plotter x langs horisontal akse og y langs vertikal akse
plt.plot(1, 2, 'bo') # plotter punktet (1,2) som blå sirkel
plt.plot(2,3, 'ro')
plt.plot(3,1, 'go')

plt.show()