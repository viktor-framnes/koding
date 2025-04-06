n=9
print("   ", end="")
for i in range(1,n+1):
    print(f"{(i):4}", end="")
print("")
print("  --------------------------------------")
for i in range(1,n+1):
    print(f"{i} |", end="")
    for j in range(1,n+1):
        print(f"{(i * j):4}", end="")
    print("")