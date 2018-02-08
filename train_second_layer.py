'''
Author : Siddharth Nayak
email:ee16b073@smail.iitm.ac.in
'''
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import scipy as sp
import os, signals1
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold
'''
This module is for the second layer of SVM to classify between gestures
having similiarity in the dynamic parts.
'''

#Check if the module is executed as main, needed for parallel processing
if __name__ == '__main__':
	#List of parameters
	SHOW_CONFUSION_MATRIX = False

	x_data = []
	y_data = []

	classes = {}

	root="data1234" #Default directory containing the dataset

	print( "Loading the dataset from '{directory}'...".format(directory=root),)
	
	#Fetch all the data files from the root directory of the dataset
	for path, subdirs, files in os.walk(root):
		for name in files:
			
			#Get the filename
			filename = os.path.join(path, name)
			if filename[-6:]!='_Store':
				print(filename)
				#Load the sample from file
				sample = signals1.Sample.load_from_file(filename)
				#Linearize the sample and then add it to the x_data list
				x_data.append(sample.get_linearized())
				#Extract the category from the file name
				#For example, the file "a_sample_0.txt" will be considered as "a"
				category = name.split("_")[0]
				#Get a number for the category, as an offset from the category
				#to the a char in Ascii
				
				if category=='d':
					number=0
				elif category=='e':
					number=1
				elif category=='i':
					number=2
				elif category=='j':
					number=3
				elif category=='g':
					number=4
				elif category=='k':
					number=5
				#Add the category to the y_data list
				y_data.append(number)
				#Include the category and the corresponding number into a dictionary
				#for easy access and referencing
				classes[number] = category
				print('done')

	print ("DONE")

	#Parameters used in the cross-validated training process
	#The library automatically tries every possible combination to
	#find the best scoring one.
	params = {'C':[0.001,0.01,0.1,1], 'kernel':['rbf']}
	#params= {'max_depth': [1, 2, 3, 4, 5],'max_features': [1, 2, 3, 4]}
	


	#Inizialize the model
	svc = svm.SVC(probability = True)
	#clf = DecisionTreeClassifier(random_state=0)
	#Inizialize the GridSearchCV with 8 processing cores and maximum verbosity
	clf = GridSearchCV(svc, params,verbose =10, n_jobs=8)
	#grid_search = GridSearchCV(clf, param_grid = params,cv = cross_validation)


	#Split the dataset into two subset, one used for training and one for testing
	X_train, X_test, Y_train, Y_test = train_test_split(x_data,
				y_data, test_size=0.35, random_state=0)
	
	

	print ("Starting the training process...")

	#Start the training process
	clf.fit(X_train, Y_train)
	

	#If SHOW_CONFUSION_MATRIX is true, prints the confusion matrix
	if SHOW_CONFUSION_MATRIX:
		print ("Confusion Matrix:")
		Y_predicted = clf.predict(X_test)
		print (confusion_matrix(Y_test, Y_predicted))

	print ("\nBest estimator parameters: ")
	#print (clf.best_estimator_)
	#print (clf.best_score_)

	#Calculates the score of the best estimator found.
	score = clf.score(X_test, Y_test)

	print ("\nSCORE: {score}\n".format(score = score))

	print ("Saving the model...",)

	#Saves the model to the "model.pkl" file
	joblib.dump(clf, 'model_flex1.pkl')
	#Saves the classes to the "classes.pkl" file
	joblib.dump(classes, 'classes_flex1.pkl')

	print ("DONE")
