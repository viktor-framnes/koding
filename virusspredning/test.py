import random

def spredning(self):
    for i in range(self.lengde):
        for j in range(self.lengde):
            if (self.personer[i][j].tilstand in [0,3,4]):
                continue
          
            if (i < 0 or i+1 > self.lengde or j < 0 or j+1 > self.lengde):
                continue
            
            if i > 0 and self.personer[i-1][j].tilstand == 0: #N
                if random.random() < 0.3:
                    self.smittetBlokk((i-1),j)
            if j < self.lengde-1 and self.personer[i][j+1].tilstand == 0: #Ø
                if random.random() < 0.3:
                    self.smittetBlokk(i,(j+1))
            if i < self.lengde-1 and self.personer[i+1][j].tilstand == 0: #S
                if random.random() < 0.3:
                    self.smittetBlokk((i+1),j)
            if j > 0 and self.personer[i][j-1].tilstand == 0: #V
                if random.random() < 0.3:
                    self.smittetBlokk(i,(j-1))
                    