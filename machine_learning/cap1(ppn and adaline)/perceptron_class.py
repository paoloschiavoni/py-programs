import numpy as np

class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta=eta
        self.n_iter=n_iter

    def net_input(self, X):
        return np.dot(X, self.w[1:])+ self.w[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def fit(self, X, y):
        '''
        X è la tabella con
            n righe= n campioni
            n colonne= n caratteristiche
        y è tabella con i risultati
        '''
        self.w=np.zeros(X.shape[1]+1)#shape da (n righe, n colonne)
        self.errors=[]
        for _ in range(self.n_iter):
            errors=0
            for xi, target in zip(X, y):
                update = self.eta*(target - self.predict(xi))
                self.w[1:] += update*xi
                self.w[0] += update
                errors+= int(update !=0.0)
            self.errors.append(errors)
        return self
