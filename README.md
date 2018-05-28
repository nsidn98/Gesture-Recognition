# Gesture-Recognition
Recognition of standard army hand gestures.

It recognises these [gestures](https://www.zombiehunters.org/wiki/index.php/Military_Hand_Signals).

## Hardware:
![Image of the glove](https://github.com/nsidn98/Gesture-Recognition/blob/master/FullSizeRender.jpg)

## Circuit(Layman):
![Circuit](https://github.com/nsidn98/Gesture-Recognition/blob/master/gesture%20recognition_bb.jpg)


## Nomenclature of data:
### Static Gestures Data: 
<gesture_name.txt> --> values of accelerometer and gyro values for the gesture `gesture_name`.

First seven columns correspond to flex sensor values: First five for five fingers respectively, 6th row for wrist and the 7th column for elbow. 

The next three columns correspond to the angles made wrt the 3 axes.

The next three are for for accelerations in 3 axes and the last three for the gyro values.

Each of the row corresponds to a different instance/datapoint of the gesture.


## Dynamic Gestures Data
[Link]{https://drive.google.com/drive/folders/1FDEr4vginXFtD69GY8WtL8kSirXTGTQ1?usp=sharing} for the Dynamic gestures data.

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
A button was provided to classify between the static and dynamic.(pretty naive)

For static gestures data the acceleration and gyro values were neglected as they were causing a lot of false positives for wrong gesture classes.So only the flex sensor values and the angle values were used in the Support Vector Machine (SVM).
As visible in the Principal Component Analysis(PCA) of the datapoints (10 dimensions projected to 3 dimensions) they are pretty much clusterable when only the flex sensor values and the angle values are used and pquite haywire when all the feature are used.

When only the above said features are used.
![PCA static](https://github.com/nsidn98/Gesture-Recognition/blob/master/PCA/Figure_1.png)
When all features are used:
![PCA static](https://github.com/nsidn98/Gesture-Recognition/blob/master/PCA/Figure_1%3D.png)
Each color(cluster) represents a gesture.

For the dynamic gesture data :


 If you face some problems or are not clear about the usage email me at [siddharthnayak98@gmail.com](mailto:siddharthnayak98gmail.com)

