import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
 

def importdata():
    balance_data = pd.read_csv('/home/nxechanges/Downloads/ipl/webapp/test2.csv')
    print ("lenght: ", len(balance_data))
    balance_data = balance_data.dropna() 
    return balance_data
 

def splitdataset(balance_data):
 
    name = balance_data.Team1.unique()
    a = balance_data.Name.astype(pd.api.types.CategoricalDtype(categories=name)).cat.codes
    balance = balance_data.drop(['Team1'],axis=1)
    balance['Team_1']=a
    # name2 = balance_data.Team2.unique()
    # a = balance_data.Name.astype(pd.api.types.CategoricalDtype(categories=name2)).cat.codes
    # balance = balance_data.drop(['Team2'],axis=1)
    # balance['Team_2']=a
    # name3 = balance_data.Venue_Name.unique()
    # a = balance_data.Name.astype(pd.api.types.CategoricalDtype(categories=name3)).cat.codes
    # balance = balance_data.drop(['Venue_Name'],axis=1)
    # balance['Venue_Name_1']=a
    # name4 = balance_data.Toss_Winner.unique()
    # a = balance_data.Name.astype(pd.api.types.CategoricalDtype(categories=name4)).cat.codes
    # balance = balance_data.drop(['Toss_Winner'],axis=1)
    # balance['Toss_Winner_1']=a

    X = balance.values['Team_1','Team_2','Venue_Name_1','Toss_Winner_1']
    Y = balance.values['match_winner']
 
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)
     
    return X, Y, X_train, X_test, y_train, y_test
     

def train_using_nb(X_train, y_train):
 
    clf_nb = GaussianNB()
    clf_nb.fit(X_train, y_train)
    return clf_nb
    
def prediction(X_test, clf_object):
 
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred
     
def cal_accuracy(y_test, y_pred):
          
    print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)
     
    
def Nbmain(context):
     
   
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    clf_nb = train_using_nb(X_train, y_train)
    # clf_entropy = tarin_using_entropy(X_train, y_train)
     
    test = [[context['team1'],context['team2'],context['venue'],context['toss']]];
    print("Results Using Gini Index:")
     
    #  #Prediction using gini
    y_pred_nb = prediction(test,clf_gini)
    print(y_pred_nb)
    return y_pred_nb

    # for i in y_pred_gini:
    #     print(i)

    # cal_accuracy(y_test, y_pred_gini)
     
    # print("Results Using Entropy:")
    # # Prediction using entropy
    # y_pred_entropy = prediction(X_test, clf_entropy)
    # cal_accuracy(y_test, y_pred_entropy)
     
    

