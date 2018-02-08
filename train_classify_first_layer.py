'''
Author : Siddharth Nayak
email:ee16b073@smail.iitm.ac.in
'''
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import scipy as sp
import os, signals
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier
import pandas as pd
x_data = []
y_data = []
classes = {}
root="dynamic data"
print( "Loading the dataset from '{directory}'...".format(directory=root),)
'''
This module is for the first layer of SVM to classify between gestures.
'''

df=[]
for path, subdirs, files in os.walk(root):
  for name in files:
    
    #Get the filename
    filename = os.path.join(path, name)
    if filename[-6:]!='_Store':
      print(filename)
      
      #Load the sample from file
      df1 = pd.read_csv(filename,delim_whitespace=False)
      #Linearize the sample and then add it to the x_data list
      df = df.append(df1)
      #Extract the category from the file name
      #For example, the file "a_sample_0.txt" will be considered as "a"
      category = name.split("_")[0]
      #Get a number for the category, as an offset from the category
      #to the a char in Ascii
      number = ord(category) - ord("a")
      #Add the category to the y_data list
      y_data.append(number)
      #Include the category and the corresponding number into a dictionary
      #for easy access and referencing
      classes[number] = category
      print('done')

print ("DONE")

x_data=df.iloc[:,0:10]
params = {'C':[0.001,0.01,0.1,1], 'kernel':['linear']}
svc1 = svm.SVC(probability = True)
clf = GridSearchCV(svc, params,verbose =10, n_jobs=8)
X_train, X_test, Y_train, Y_test = train_test_split(x_data,y_data, test_size=0.35, random_state=0)
print ("Starting the training process...")
clf.fit(X_train, Y_train)
score = clf.score(X_test, Y_test)
print ("\nSCORE: {score}\n".format(score = score))
joblib.dump(clf, 'model1.pkl')
joblib.dump(classes, 'classes1.pkl')
