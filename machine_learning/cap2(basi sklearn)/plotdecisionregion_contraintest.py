import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_decision_region(X, y, classifier, resolution=0.02, test_idx=None):
    markers=('s', 'x', '^', 'o', 'v')
    colors=('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap=ListedColormap(colors[:len(np.unique(y))])#in questo caso [2]

    x1_min, x1_max=X[:, 0].min()-1, X[:, 0].max() +1
    x2_min, x2_max=X[:, 1].min()-1, X[:, 1].max()+1
    xx1, xx2=np.meshgrid(np.arange(x1_min, x1_max, resolution), \
        np.arange(x2_min, x2_max, resolution))#grid con i valori che vanno da min a max con intervalli di resolution
    Z=classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)#sta roba nelle parentesi è X infatti .T mi da lo stesso formato di X
    Z=Z.reshape(xx1.shape)#porto alle dimensioni di xx1
    plt.contourf(xx1, xx2, Z, alpha=0.2, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):#idx è l'index (in questo caso dato che len(y)=2 può essere 0 o 1. cl è il valore 1 o -1 (setosa o no)
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], alpha=0.8, c=cmap(idx), \
            marker=markers[idx], label=cl)

    #disegna dei cerchi intorno ai campioni di test
    if test_idx: #test idx è la lista dei campioni che fanno parte del test. se sono messi, sono diversi da None
        X_test, y_test=X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='black', marker='o', label='campioni test', alpha=0.5)
