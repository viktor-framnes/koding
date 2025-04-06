import pandas as pd
import matplotlib.pyplot as plt

filnavn = "Datasett_fodselstall.csv"

df = pd.read_csv(filnavn, sep="\t", encoding="utf-8", na_values="..") # bruker na_values=".." for å kunne regne selv om det ikke var noen verdier i csv filen, trengs for oppgave b)



