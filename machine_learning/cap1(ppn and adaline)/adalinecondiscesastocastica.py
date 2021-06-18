import numpy as np

class Adaline_stoc(object):

    def __init__(self, n_iter=10, eta=0.1, shuffle=True):
        self.n_iter=n_iter
        self.eta=eta
        self.shuffle_bool=shuffle

    def fit(self, X, y):
        self.w_=np.zeros(X.shape[1]+1)
        self.cost_list=[]
        for i in range(self.n_iter):
            if self.shuffle_bool:
                X, y=self.shuffle(X, y)
            cost_tmp=[]
            for xi, target in zip(X, y):
                cost_tmp.append(self.update_w(xi, target))
            avg_cost=sum(cost_tmp)/len(y)
            self.cost_list.append(avg_cost)
        return self

    def shuffle(self, X, y):
        r=np.random.permutation(len(y))
        return X[r], y[r]

    def update_w(self, xi, target):
        #adaline learning rule
        output=self.net_input(xi)
        error=target-output
        self.w_[1:]+= self.eta*xi.dot(error)
        self.w_[0]+= self.eta*error
        cost =0.5*error**2
        return cost

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return self.net_input(X)
    def predict(self, X):
        return np.where(self.activation(X)>=0.0, 1, -1)
