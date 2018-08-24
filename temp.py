import xlrd

from sklearn.cluster import KMeans
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt

file_location = "data1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_name('B1')

x = []
for value in sheet.col_values(3):
    value = int(value)
    val = ((value-300)/(14000-300))*(100-0)+0
    x.append(val)


y = []
for value in sheet.col_values(7):
    value = int(value)
    val = ((value-100)/(600-100))*(100-0)+0
    y.append(val)

X = np.array(list(zip(x, y))).reshape(len(y), 2)
# KMeans algorithm 
K = 12
kmeans_model = KMeans(n_clusters=K).fit(X)
 
label = 0

for row in range(sheet.nrows):
    for column in range(sheet.ncols):
        if sheet.cell(row, column).value == "SL Malinga (SL)":  
            reqrow = row
            label = kmeans_model.labels_[row]

pl_run= sheet.cell(reqrow,3)   
pl_avg = sheet.cell(reqrow,7)

print('Your players stats:')

print(pl_avg,pl_run)    
        
print('You should also see these players:')

for i, l in enumerate(kmeans_model.labels_):
    if kmeans_model.labels_[i] == label:
        value = sheet.cell(i,0)
        print(value)
        value = sheet.cell(i,3)
        print(value)
        value = sheet.cell(i,7)
        print(value)
        
               

