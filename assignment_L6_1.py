# -*- coding: utf-8 -*-
# Zadanie 1 (7 pkt.)
"""
Kod muszą państwo zaimplementować w pliku `assignment_L6_1.py`, a gotowe zadanie oddajemy wypychając zmiany na repozytorium.

+ Załaduj zbiór danych __iris__ korzystając z funkcji [load_iris](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
+ Korzystając z funkcji [SelectKBest](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html)
oraz kryterium [mutual_info_classif](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif)
wybierz najlepsze __dwa__ atrybuty 
+ Korzystając z [tego](http://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)
 przykładu wyświetl na jednym wykresie granice decyzyjne dla następujących klasyfikatorów:
 + KNN z liczbą najbliższych sąsiadów 1;
 + Liniowy SVM;
 + SVM z jądrem RBF;
 + Naive Bayes;
 + Drzewa dacyzyjnego o maksymalnej głębokosci 10.
 
"""
from itertools import product

import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from matplotlib import pyplot as plt
import numpy as np
from sklearn import feature_selection


from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier



def load_iris_data_set():
    ds = datasets.load_iris()
    X = ds.data
    y = ds.target
    ds.feature_names
    return X, y

def select_k_best(criteria, X, y):
    clf = feature_selection.SelectKBest(criteria,k=2)
    X = clf.fit_transform(X, y)
    return X

X, y = load_iris_data_set()
X = select_k_best(feature_selection.mutual_info_classif, X, y)
print X

clf1 = KNeighborsClassifier(n_neighbors=1)
clf2 = LinearSVC()
clf3 = SVC(kernel='rbf', probability=True)
clf4 = GaussianNB()
clf5 = DecisionTreeClassifier(max_depth=10)

clf1.fit(X, y)

clf2.fit(X, y)

clf3.fit(X, y)

clf4.fit(X, y)

clf5.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

f, axarr = plt.subplots(3, 2, sharex='col', sharey='row', figsize=(10, 8))

for idx, clf, tt in zip(product([0, 1, 2], [0, 1]),[clf1, clf2, clf3, clf4, clf5],[' KNN  1', 'Liniowy SVM',
                                                        'SVM RBF', 'Naive Bayes', 'Drzewa dacyzyjnego 10']):

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    axarr[idx[0], idx[1]].contourf(xx, yy, Z, alpha=0.4)
    axarr[idx[0], idx[1]].scatter(X[:, 0], X[:, 1], c=y,
                                  s=20, edgecolor='k')
    axarr[idx[0], idx[1]].set_title(tt)

plt.show()

#!!7