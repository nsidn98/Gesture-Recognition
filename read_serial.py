'''
Author : Siddharth Nayak
email:ee16b073@smail.iitm.ac.in
'''

import serial
import re
import time
import numpy as np
from sklearn.svm import SVC
import pandas as pd
from sklearn.externals import joblib
'''
This module is for real time prediction of the static gestures
'''

clf = joblib.load('~/Downloads/model_static_angle.pkl')
print('Model Loaded')
#read the data into a dataframe
'''
To train static gestures for the first time uncomment this snippet
df=pd.read_csv('~/Downloads/data2/data.txt',header=None,delim_whitespace=True)
df = df.sample(frac=1).reset_index(drop=True)
df = df.sample(frac=1).reset_index(drop=True)
y=df[10]
X=df.iloc[:,0:10]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
clf=SVC(kernel='linear',C=1).fit(X_train,y_train)
clf1=SVC(kernel='rbf',C=1).fit(X_train,y_train)'''

#open the serial port to read
ser =serial.Serial('/dev/cu.usbmodem1421',38400,timeout=None) #change it according to your port
x=np.zeros(10)
i=0
time.sleep(2)
print('Initializing all Systems')
while 1:
	i+=1
	try:
		a=ser.readline()
		c=a.decode('ASCII')

		time.sleep(0.01)

	except ser.SerialTimeoutException:
		print('Data could not be read')
		time.sleep(1)
	if(i<10):
		continue

	else:
		b=c.split()
		b=[float(x) for x in b]
		x+=b
		x.reshape(1,-1)

		if i%20==0:
			#print(x/20)

		#	print(x/10)
			if(clf.predict([list(x/20)])==1):
				print('One')
			if(clf.predict([list(x/20)])==2):
				print('Two')
			if(clf.predict([list(x/20)])==3):
				print('Three')
			if(clf.predict([list(x/20)])==4):
				print('Four')
			if(clf.predict([list(x/20)])==5):
				print('Five')
			if(clf.predict([list(x/20)])==6):
				print('Six')
			if(clf.predict([list(x/20)])==7):
				print('Seven')
			if(clf.predict([list(x/20)])==8):
				print('Eight')
			if(clf.predict([list(x/20)])==9):
				print('Nine')
			if(clf.predict([list(x/20)])==10):
				print('Ten')
			if(clf.predict([list(x/20)])==11):
				print('You')
			if(clf.predict([list(x/20)])==12):
				print('Me')
			if(clf.predict([list(x/20)])==13):
				print('Listen or I Hear')
			if(clf.predict([list(x/20)])==14):
				print('Watch or I See')
			if(clf.predict([list(x/20)])==15):
				print('Stop')
			if(clf.predict([list(x/20)])==16):
				print('Freeze')
			if(clf.predict([list(x/20)])==17):
				print('Cover this Area')
			if(clf.predict([list(x/20)])==18):
				print('Enemy')
			if(clf.predict([list(x/20)])==19):
				print('Hostage')
			if(clf.predict([list(x/20)])==20):
				print('Sniper')
			if(clf.predict([list(x/20)])==21):
				print('Dog')
			if(clf.predict([list(x/20)])==22):
				print('Cell Leader')
			if(clf.predict([list(x/20)])==23):
				print('Line Abreast Formation')
			if(clf.predict([list(x/20)])==24):
				print('Pistol')
			if(clf.predict([list(x/20)])==25):
				print('Rifle')
			if(clf.predict([list(x/20)])==26):
				print('I Understand')
			if(clf.predict([list(x/20)])==27):
				print('Breacher')
			if(clf.predict([list(x/20)])==28):
				print('Gas')

			x=np.zeros(10)
