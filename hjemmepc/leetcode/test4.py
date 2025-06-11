# s1 = "bank"
# s2 = "kanb"
# n = len(s1)
# teller = 0

# for y, i in enumerate(s1):
#     if i == s2[y]:
#         teller += 1

# if teller >= len(s1)-2:
#     print(True)
# else:
#     print(False)


l = [2,4,6]
l.sort()

a = max(l) - min(l)
for i in range(len(l)):
    if l[i] != max(l) or l[i] != min(l):
        c = l[i]

if c == a:
    print(a + c)
elif c < a:
    print(a + c)

if c == a:
    print()