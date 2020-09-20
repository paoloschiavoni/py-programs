class Card(object):

    RANKS=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    SEMI=["cuori", "quadri", "fiori", "picche"]

    def __init__(self, rank, seme):
        self.rank=rank
        self.seme=seme

    def __str__(self):
        return str(self.rank)+ " di " + str(self.seme)

    def getRank(self):
        rank, seme=self.rank, self.seme
        return rank
