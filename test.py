import numpy as np
import pandas as pd
from sklearn import preprocessing


balance_data = pd.read_csv('test.csv')
print(list(balance_data.columns.values))

names = balance_data.Name.unique()
print(names)
a = balance_data.Name.astype(pd.api.types.CategoricalDtype(categories=names)).cat.codes

balance_data['match_winner_1']=pd.Series(a,index=balance_data.index)
print(balance_data)
# print(balance_data.add(a,axis=1))
# print(a.values)
# X = balance_data.values[:,1:4];
# print(X.shape,a.shape)
print(type(a.as_matrix()))
#print(np.append(X,a.as_matrix(),axis=1))


# trans = balance_data.values[:,4]
# import ipdb; ipdb.set_trace()
# le=preprocessing.LabelEncoder()
# le.fit(trans)
# print(le.classes_)
# a = le.transform(["A Ashish Reddy"])
# print(type(trans))
# print(balance_data..astype('category', categories=le.classes_).cat.codes)
#X = balance_data.values[:,3]
# print(a)
