# Et lite eksempel på hvordan vi kan plotte i python
# For å installere: pip install matplotlib
import matplotlib.pyplot as plt 

x_list = [1,2,3,4,5]
y_list = [5,4,3,2,1]
y2_list = [6,7,8,9,10]

plt.plot(x_list, y_list)
plt.plot(x_list, y2_list)
plt.title("Første forsøk på plotting")
plt.xlabel("Tid")
plt.ylabel("Antall")
plt.show("") #Brukes for å vise plottet
plt.savefig("Navn_på_fil") #Brukes for å lagre bilde av plottet. Legg inn string med lagringssted eksempel: "C:/User/mahea182/it2/file_name"