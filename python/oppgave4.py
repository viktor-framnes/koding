s = int(input("Skriv inn sidelengden: "))

for i in range(s):
    if i >= 2 and i < s-2:
        print("##", end="")
        print(" "*(s-4), end="")
        print("##")
    else:
        print("#"*s)