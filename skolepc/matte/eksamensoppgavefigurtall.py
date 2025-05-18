# # Pn-1 + 5 (n-1)


# def funk(n):
#     if n == 1:
#         return 1
#     return funk(n-1)+5*(n-1)

# print(funk(100))

S = 1
n = 1

while n < 50:
    S += (n+1)**3
    n += 1

print(n)
print(S)