'''
Author : Siddharth Nayak
email:ee16b073@smail.iitm.ac.in
'''

import numpy as np
from sklearn.preprocessing import scale
from scipy.interpolate import interp1d
'''
library for getting the values with only few parameters
'''
class Sample:
    def __init__(self,flex1,flex2,flex3,flex4,flex5,flex6,flex7,angx,angy,angz):
        
        self.flex1=flex1
        self.flex2=flex2
        self.flex3=flex3
        self.flex4=flex4
        self.flex5=flex5
        self.flex6=flex6
        self.flex7=flex7
        '''self.acx=acx
        self.acy = acy
        self.acz = acz
        self.gx = gx
        self.gy = gy
        self.gz = gz'''
        self.angx=angx
        self.angy=angy
        self.angz=angz

    def get_linearized(self,reshape=False):
        if reshape:
            return np.concatenate((self.flex1,self.flex2,self.flex3,self.flex4,self.flex5,self.flex6,self.flex7,self.angx,self.angy,self.angz)).reshape(1,-1)
        else:
            return np.concatenate((self.flex1,self.flex2,self.flex3,self.flex4,self.flex5,self.flex6,self.flex7,self.angx,self.angy,self.angz))

    @staticmethod
    def load_from_file(filename,size_fit=50):
        data_raw=[]
        for i in open(filename):
            data_raw.append(list(float(x) for x in i.split()))
        #Load the signal data from the file as a list

        #Convert the data into floats
        data = np.array(data_raw).astype(float)

		#Standardize the data by scaling it
        data_norm = scale(data)

        #Extract each axe into a separate variable
		#These represent the acceleration in the 3 axes
        flex1=data_norm[:,0]
        flex2=data_norm[:,1]
        flex3=data_norm[:,2]
        flex4=data_norm[:,3]
        flex5=data_norm[:,4]
        flex6=data_norm[:,5]
        flex7=data_norm[:,6]
        
        angx=data_norm[:,7]
        angy=data_norm[:,8]
        angz=data_norm[:,9]
        
        '''acx = data_norm[:,10]
        acy = data_norm[:,11]
        acz = data_norm[:,12]

        #These rapresent the rotation in the 3 axes
        gx = data_norm[:,13]
        gy = data_norm[:,14]
        gz = data_norm[:,15]'''

        #Create a function for each axe that interpolates the samples
        x = np.linspace(0, data.shape[0], data.shape[0])
        f_flex1=interp1d(x, flex1)
        f_flex2=interp1d(x, flex2)
        f_flex3=interp1d(x, flex3)
        f_flex4=interp1d(x, flex4)
        f_flex5=interp1d(x, flex5)
        f_flex6=interp1d(x, flex6)
        f_flex7=interp1d(x, flex7)
        
        '''f_acx = interp1d(x, acx)
        f_acy = interp1d(x, acy)
        f_acz = interp1d(x, acz)

        f_gx = interp1d(x, gx)
        f_gy = interp1d(x, gy)
        f_gz = interp1d(x, gz)'''

        f_angx = interp1d(x, angx)
        f_angy = interp1d(x, angy)
        f_angz = interp1d(x, angz)

		#Create a new sample set with the desired sample size by rescaling
		#the original one
        xnew = np.linspace(0, data.shape[0], size_fit)
        flex1_stretch = f_flex1(xnew)
        flex2_stretch = f_flex2(xnew)
        flex3_stretch = f_flex3(xnew)
        flex4_stretch = f_flex4(xnew)
        flex5_stretch = f_flex5(xnew)
        flex6_stretch = f_flex6(xnew)
        flex7_stretch = f_flex7(xnew)
        
        '''acx_stretch = f_acx(xnew)
        acy_stretch = f_acy(xnew)
        acz_stretch = f_acz(xnew)

        gx_stretch = f_gx(xnew)
        gy_stretch = f_gy(xnew)
        gz_stretch = f_gz(xnew)'''

        angx_stretch = f_angx(xnew)
        angy_stretch = f_angy(xnew)
        angz_stretch = f_angz(xnew)

		#Returns a Sample with the calculated values
        return Sample(flex1_stretch,flex2_stretch,flex3_stretch,flex4_stretch,flex5_stretch,flex6_stretch,flex7_stretch,angx_stretch,angy_stretch,angz_stretch)
