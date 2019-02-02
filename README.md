# Gesture-Recognition
Recognition of standard army hand gestures.
Soldiers communicate with each other through gestures. But sometimes those gestures are not visible due to obstructions or poor lighting. For that purpose an instrument is required to record the gesture and send it to the fellow soldiers. The two options for gesture recognition are through Computer Vision and through some sensors attached to the hands.The first option is not viable in this case as proper lighting is required for recognition through Computer Vision. Hence the second option of using sensors for recognitions has been used. We present a system which recognises the gestures shown below:

![Gestures](https://github.com/nsidn98/Gesture-Recognition/blob/master/Images/gestures.jpg)

## Construction
The given gestures include motions of fingers, wrist and elbow.Hence to detect any changes in them we have used one flex sensors which detects the amount by which it has been bent at each of these joints. To take into account for the dynamic gestures an Inertial Measurement Unit(IMU-MPU-9250) was used.The parameters used from the IMU are Acceleration,Gyroscopic acceleration and angles in all three axes.An Arduino Mega was used to receive the signals from the sensors and send it to the processor.

## Hardware:
![Image of the glove](https://github.com/nsidn98/Gesture-Recognition/blob/master/FullSizeRender.jpg)

## Things Required:
* Flex Sensors x 7
* Inertial Measurement Unit(MPU-6050 or MPU9250) x 2
* Arduino Mega or Raspberry Pi x 1
* Glove x 1
* Elbow Band x 1
* Wrist band x 1
* General Circuit Board
* Push Button
* Resistors


## Circuit(Layman):
![Circuit](https://github.com/nsidn98/Gesture-Recognition/blob/master/gesture%20recognition_bb.jpg)


## Nomenclature of data:
### Static Gestures Data:
`gesture_name.txt`: values of accelerometer and gyro values for the gesture `gesture_name`.

First seven columns correspond to flex sensor values: First five for five fingers respectively, 6th row for wrist and the 7th column for elbow.

The next three columns correspond to the angles made wrt the 3 axes.

The next three are for for accelerations in 3 axes and the last three for the gyro values.

Each of the row corresponds to a different instance/datapoint of the gesture.


## Dynamic Gestures Data
[Link](https://drive.google.com/drive/folders/1FDEr4vginXFtD69GY8WtL8kSirXTGTQ1?usp=sharing) for the Dynamic gestures data.

Nomenclature for file name:
`d_sample_0_13.txt`: `d` stands for the gesture corresponding to `d`(here Column Formation)

`0` stands for the recording session number.(You don't have to worry about it if you.

`13` stands for the datapoint number, as each file represents a single instance of the gesture. Each gesture has approximately 60 datapoints.(took a lot of pain to record each of them)

Each of the file is a sequence of values obtained through the sensors. (people can try out LSTMs too) So each datapoint is (7+3+3+3)x(length of the file) where (7+3+3+3) are the features mentioned above. The length of the file basically signifies the number of timesteps for which the gesture is carried out.(Remember the MPU6050 or MPU9250 gives sampled data).


| Code in data | Gesture name|
|--------------|-------------:|
|a|Come|
|b|Hurry up|
|c|Go Here or Move U|
|d|Column Formation|
|e|File Formation|
|f|Wedge Formation|
|g|Rally Point|
|h|Shotgun|
|i|Ammunition|
|j|Vehicle|
|k|I don't Understand|
|l|Crouch or Go Prone|
|m|Window|
|n|Door|
|o|Point of Entry|
					
					
					
					
# Algorithm:
A button was provided to start the gesture for both the static and dynamic gestures.(pretty naive).i.e. the user has to press button 'A' if he/she wants to make a static gesture and press button 'B' for the dynamic gesture.

After the button is pressed the Arduino starts recording the sensor values. These sensor values are then preprocessed.

## Preprocessing of the data:
The data collected would vary according to the gesture.
### Static Gesture:
If it is a static gesture, then the data collected would be like:
```
96 520 507 236 181 221 162 9.86	-62.82 3.73 14411.55 1251.89 7263.08 140.94 34.29 31.60
96 520 506 236 181 222 162 9.83	-62.78 3.70 14402.97 1244.89 7267.33 150.29 33.63 33.22
95 520 506 235 181 221 161 9.87	-62.76 3.69 14385.42 1241.65 7280.36 169.43 16.54 30.71
96 520 507 235 181 221 161 9.93	-62.75 3.71 14376.95 1244.77 7301.54 184.90 -15.83 29.67
96 520 507 236 182 222 161 10.05 -62.81 3.74 14375.51 1252.93 7297.46 182.21 -31.64 37.64
```
The size of the data captured would `16 x t` where `t` is the amount of time for which the button is pressed. Also, in static gestures we just use the first 10 features(reason for it is given below). So here `t` is variable which means that we have a sequential data. This rings bells for using a `Recurrent Neural Network(RNN)` but using it means we need more data and higher processing power which certainly mean that it would not be mobile. So we have to use some clever trick to handle this sequential data. So we use `SVMs(Support Vector Machine)` which is often called a poor man's neural network for classification. This is a method which uses neat and elegant methods to come up with maximal margin boundaries or gutters as Dr.Patrick Winston likes to call it. So here we collect `10 x t` data for each gesture and then sample 50 points out of it giving us a `10 x 50 ` vector. If `t<50` then we use extrapolation to make it of size `10 x 50`. Now this vector is linearised and fed to train on an SVM with Radial Basis Function Kernel(Gaussian). The training is super-fast compared to Neural Nets and certainly RNNs.

### Dynamic Gesture:

The size of the data captured would `16 x t` where `t` is the amount of time for which the button is pressed. The only difference between the static and dynamic being that instead of `10 x t` as in static we use `16 x t` to sample from. Again we get a `16 x 50` vector which is linearised and fed to train on an SVM.


### Reason for using `10 x 50 vector` in static and `16 x t vector` in dynamic
For static gestures data, the acceleration and gyro values were neglected as they were causing a lot of false positives for wrong gesture classes.So only the flex sensor values and the angle values were used in the Support Vector Machine (SVM).
As visible in the Principal Component Analysis(PCA) of the datapoints they are pretty much clusterable when only the flex sensor values and the angle values are used and quite haywire when all the feature are used.

Another point to be noteed was that the PCA shows us that there is a lot of room to add more gestures as the clusters are quite far apart.

When only the above said features are used.
![PCA static](https://github.com/nsidn98/Gesture-Recognition/blob/master/PCA/Figure_1.png)
When all features are used:
![PCA static](https://github.com/nsidn98/Gesture-Recognition/blob/master/PCA/Figure_1%3D.png)
Each color(cluster) represents a gesture.

### Sampling Method
In plots below sampling makes the data points of the same gesture have a same shape as seen in the last row of the both examples for `door` as well as `window`. So the SVM is actually trying to capture the shape of the signal amplitude in time domain.

One of the samples for gesture `door`|  Another sample for gesture `door`
:-------------------------:|:-------------------------:
![](https://github.com/nsidn98/Gesture-Recognition/blob/master/Images/G1.png)  |  ![](https://github.com/nsidn98/Gesture-Recognition/blob/master/Images/G2.png)

One of the samples for gesture `door`|  Another sample for gesture `window`
:-------------------------:|:-------------------------:
![](https://github.com/nsidn98/Gesture-Recognition/blob/master/Images/G3.png)  |  ![](https://github.com/nsidn98/Gesture-Recognition/blob/master/Images/G4.png)


 If you face some problems or are not clear about the usage email me at [siddharthnayak98@gmail.com](mailto:siddharthnayak98gmail.com)

