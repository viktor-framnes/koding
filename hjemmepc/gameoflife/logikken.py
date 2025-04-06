import random

class Gameoflife:
    def __init__(self,lengde):
        self.lengde = lengde
        self.brett = [[0 for i in range(self.lengde)] for j in range(self.lengde)]

        for n in range(self.lengde):
            for m in range(self.lengde):
                if random.random() < 0.3:
                    self.brett[n][m] = 1
                else:
                    self.brett[n][m] = 0


    def kjor(self):
        for n in range(self.lengde):
            for m in range(self.lengde):
                naboer = self.tellnaboer(n,m)
                if self.brett[n][m] == 1:
                    if naboer in [2,3]: 
                        self.brett[n][m] = 3
                elif naboer == 3:
                    self.brett[n][m] = 2

        for n in range(self.lengde):
            for m in range(self.lengde):
                if self.brett[n][m] == 1:
                    self.brett[n][m] = 0
                elif self.brett[n][m] in [2,3]:
                    self.brett[n][m] = 1

    def tellnaboer(self,n,m):
        naboer = 0
        for i in range(n-1,n+2):
            for j in range(m-1,m+2):
                if ((i==n and j==m) or i<0 or j<0 or i==self.lengde or j==self.lengde):
                    continue
                if self.brett[i][j] in [1,3]:
                    naboer += 1
        return naboer

    

if __name__ == "__main__":
    x = Gameoflife(10)
    for rad in x.brett:
        print(rad)
    x.kjor()
    print()
    for rad in x.brett:
        print(rad)
