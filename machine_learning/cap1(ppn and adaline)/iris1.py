import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)

y=df.iloc[0:100, 4].values
y=np.where(y=='Iris-setosa', -1, 1)
X=df.iloc[0:100, [0, 2]].values
#standardizza X
X_std=np.copy(X)
X_std[:, 0]= (X[:, 0]-X[:, 0].mean()) / X[:, 0].std()
X_std[:, 1]= (X[:, 1]-X[:, 1].mean()) / X[:, 1].std()

'''
#grafico dei dati
plt.scatter(X[:50, 0], X[:50, 1], color="red", marker="o", label="setosa")
plt.scatter(X[50:100, 0], X[50:100, 1], color="blue", marker="x", label="versicolor")
plt.xlabel("sepal lenght")
plt.ylabel("petal lenght")
plt.legend(loc="upper left")
plt.show()
'''

'''
#tabella con errori
from perceptron_class import Perceptron
ppn=Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors)+1), ppn.errors, marker="o")
plt.xlabel("epoch")
plt.ylabel("numero di errori")
plt.show()
'''

'''
#disegna regione e linea che divide i due gruppi nel grafico
from plotdecisionregion import plot_decision_region
from perceptron_class import Perceptron
ppn=Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plot_decision_region(X, y, ppn)
plt.xlabel("sepal length")
plt.ylabel("petal length")
plt.legend(loc="upper left")
plt.show()
'''

'''
#grafico con errori usando adaline
from adaline_class import Adaline
fig, ax= plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
ada1=Adaline(n_iter=10, eta=0.0001).fit(X_std, y)
ax[0].plot(range(1, len(ada1.cost)+1), ada1.cost, marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('cost')
ax[0].set_title('cost with eta=0.0001')
ada2=Adaline(n_iter=10, eta=0.01).fit(X_std, y)
ax[1].plot(range(1, len(ada2.cost)+1), ada2.cost, marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('cost')
ax[1].set_title('cost with eta=0.01')
plt.show()
'''

'''
#grafico regioni con adaline+grafico errori
from adaline_class import Adaline
from plotdecisionregion import plot_decision_region
ada=Adaline(n_iter=20, eta=0.01)
ada.fit(X_std, y)
plot_decision_region(X_std, y, classifier=ada)
plt.title('adaline standardized')
plt.xlabel('sepal lenght')
plt.ylabel('petal lenght')
plt.legend(loc='upper left')
plt.show()
plt.plot(range(1, len(ada.cost)+1), ada.cost, marker='o')
plt.xlabel('epochs')
plt.ylabel('cost')
plt.show()
'''

#grafico regione adaline+grafico errori (con discesa gradiente stocastica)
from adalinecondiscesastocastica import Adaline_stoc
from plotdecisionregion import plot_decision_region
ada=Adaline_stoc(n_iter=10, eta=0.01)
ada.fit(X_std, y)
plot_decision_region(X_std, y, classifier=ada)
plt.title('adaline stoc')
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc='upper left')
plt.show()
plt.plot(range(1, len(ada.cost_list)+1), ada.cost_list, marker='o')
plt.title('errors')
plt.xlabel('epochs')
plt.ylabel('cost')
plt.show()
