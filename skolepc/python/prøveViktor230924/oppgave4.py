alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
m = int(input("Hvor mange rader: "))
n = int(input("Hvor mange kolonner: "))
print("      ", end="")
for i in range(m):
    print(f"{alf[i]:5}", end="")
print("")
for i in range(n+1):
    print(f"{i}  ", end="")
    for j in range(m):
        print(f"{j:3},{i}", end="")
    print("")