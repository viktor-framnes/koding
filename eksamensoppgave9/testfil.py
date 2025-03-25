
class Person():
    def __init__(self):
        self.dagersyk = 0

    def dag(self):
        self.dagersyk += 1

    def __str__(self):
        return f"jeg er {self.dagersyk} dager syk"


brett = [[Person() for i in range(5)] for j in range(5)]

brett[4][4] = 1
# brett[4][5].dag()
# brett[5][4].dag()

# print(brett[5][5])
# print(brett[4][4])
# print(brett[5][4])

print(brett)

    