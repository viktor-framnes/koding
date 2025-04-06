navn = "Pål"
karakterer = [3, 4, 6, 6, 5, 4]
karaktertekst = ""
for i in range(len(karakterer)):
  if i > 0 and i < (len(karakterer)-1):
    karaktertekst += ", " 
  if i == (len(karakterer)-1):
    karaktertekst += " og "
  karaktertekst += str(karakterer[i])

print(f"{navn} fikk karakterene {karaktertekst}")