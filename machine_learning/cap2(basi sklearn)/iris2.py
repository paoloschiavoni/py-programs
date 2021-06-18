from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

iris=datasets.load_iris()
X=iris.data[:, [2, 3]]
y=iris.target

#divisione in train(su cui si basa il modello) e test (su cui si testa il modello usando dati nuovi)
from sklearn. model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=0)

#standardizzazione
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
X_tot_std=np.vstack((X_train_std, X_test_std))
y_tot=np.hstack((y_train, y_test))

'''
#perceptron di skleanrn
from sklearn.linear_model import Perceptron
ppn=Perceptron(max_iter=400, eta0=0.01)
ppn.fit(X_train_std, y_train)

y_pred=ppn.predict(X_test_std)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

from plotdecisionregion_contraintest import plot_decision_region
plot_decision_region(X=X_tot_std, y=y_tot, classifier=ppn)#nel caso sapessi l'index degli elementi di test, lo potrei mettere
plt.xlabel('lunghezza_petalo')
plt.ylabel('larghezza petalo')
plt.legend(loc='upper left')
plt.show()
'''

from sklearn.linear_model import LinearRegression
from plotdecisionregion_contraintest import plot_decision_region
lr=LinearRegression()
lr.fit(X_train, y_train)
plot_decision_region(X_tot_std, y_tot, classifier=lr)
plt.xlabel("lunghezza petalo")
plt.ylabel("larghezza petalo")
plt.legend(loc='upper left')
plt.show()
