from sklearn import tree
# 1st col->> weigth
#2nd col--> 1 means smooth ,0 means bumpy
features=[[140,1],[130,1],[150,0],[170,0]]
# 0-->apple , 1--> orange
labels=[0,0,1,1]

clf=tree.DecisionTreeClassifier()

clf=clf.fit(features,labels)

print clf.predict([[150,0]])


