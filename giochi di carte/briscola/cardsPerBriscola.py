class Card(object):

    RANKS=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    SEMI=["bastoni", "coppe", "spade", "denari"]
    VALUES=[0, 2, 3, 4, 10, 11]

    
    def __init__(self, seme, rank):
        self.rank=rank
        self.seme=seme
        self.value=0
        self.getValue()
        

    def getValue(self):
        if self.rank in (2, 4, 5, 6, 7):
            self.value=0
        elif self.rank == 8:
            self.value=2
        elif self.rank == 9:
            self.value = 3
        elif self.rank == 10:
            self.value=4
        elif self.rank == 1:
            self.value = 11
        elif self.rank == 3:
            self.rank=10
        return self.value
