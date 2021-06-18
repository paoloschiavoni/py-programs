import numpy as np

class Adaline(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta=eta
        self.n_iter=n_iter

    def fit(self, X, y):
        self.w=np.zeros(X.shape[1]+1)
        self.cost=[]
        for i in range(self.n_iter):
            output=self.net_input(X)
            errors=y-output
            self.w[1:]+= self.eta*X.T.dot(errors)
            self.w[0]+= self.eta*errors.sum()
            cost=(errors**2).sum()/2.0
            self.cost.append(cost)
        return self

    def activation(self, X):
        return self.net_input(X)

    def predict(self, X):
        return np.where(self.activation(X) >= 0.0, 1, -1)

    def net_input(self, X):
        return np.dot(X, self.w[1:])+self.w[0]
