from sklearn import svm
X = [[0, 0], [1,1]]
y = [0, 1]
clf = svm.LinearSVC()
clf.fit(X, y)

clf.predict([[0.5, 0.3]])
#%%