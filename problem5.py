


from sklearn import svm
import numpy as np
import itertools
import matplotlib.pyplot as plt

X = [[0,0],[1,1],[1,0],[0,1]]
y = [0,0,1,1]
clf = svm.NuSVC()
clf.fit(X,y)
print "2-feature"
print "support vectors: ",clf.support_vectors_

def get_y(X):
	y = []
	for i in X:
		if np.sum(i) % 2 == 0:
			y.append(0)
		else:
			y.append(1)
	return y

n = 8
print n,"feature:"
lst = map(list,itertools.product([0,1],repeat=n))
X2 = np.asarray(lst)
y2 = get_y(X2)
clf.fit(X2,y2)
margin1 = 1/np.sqrt(np.sum(clf.dual_coef_**2))
print "original margin: ", margin1

sv = clf.support_vectors_.astype(int)
y_sv = get_y(sv)
clf.fit(sv,y_sv)
margin2 = 1 / np.sqrt(np.sum(clf.dual_coef_**2))

print "margin after remove non-support vectors: ", margin2
sv2 = sv[2:]
y_sv2 = get_y(sv2)
clf.fit(sv2,y_sv2)
margin3 = 1 / np.sqrt(np.sum(clf.dual_coef_**2))
print "margin after remove support vectors: ", margin3

