class Rat(object):

    """Questo programma permette di lavorare con le frazioni"""

    def __init__(self, numeratore, denominatore):
        self._num=numeratore
        self._den=denominatore
        self.reduce()

    def numeratore(self):
        return self._num
    def denominatore(self):
        return self._denominatore

    def __str__(self):
        return str(self._num) +"/"+ str(self._den)

    def reduce(self):
        divisore=self.mcd(self._num, self._den)
        self._num = self._num/divisore
        self._den =self._den/divisore

    def mcd(self, a, b):
        (a, b)=(max(a, b), min(a, b))
        while b>0:
            (a, b)=(b, a%b)
        return a

    """Definiamo le operazioni principali, self e a siniztra, other a destra"""

    def __sum__(self, other):
        newNum=self._num*other._den + other._num*self._den
        newDen=self._den*other._den
        return Rat(newNum, newDen)

    def __sub__(self, other):
        newNum=self._num*other._den - other._num*self._den
        newDen=self._den*other._den
        return Rat(newNum, newDen)

    def __per__(self, other):
        newNum=self._num*other._num
        newDen=self._den*other._den
        return Rat(newNum, newDen)

    def __div__(self, other):
        newNum=self._num*other._den
        newDen=self._den*other._num
        return Rat(newNum, newDen)


    """Definiamo ora le operazioni di uguaglianza e maggioranza"""

    def __mag__(self, other):
        return self._num*other._den>self._den*other._num

    def __magOug__(self, other):
        return self._num*other._den>=self._den*other._num

    def __ug__(self, other):
        if type(self) != type(other):
            return "Babbeo non c'entra, uno è un numero, l'altro no!"
        elif self is other:
            return True
        else:
            return False
