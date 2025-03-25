
class Person():
    def __init__(self):
        self.dagersyk = 0

    def dag(self):
        self.dagersyk += 1

    def __str__(self):
        return f"jeg er {self.dagersyk} dager syk"

brett = []
for i in range(11):
    brett.append([Person()]*11)

brett[5][5].dag()

print(brett[5][5])

# print(brett)

    