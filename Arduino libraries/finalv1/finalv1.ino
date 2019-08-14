#include<Wire.h>
int pushButton = 2;
unsigned long lastDebounceTime = {0}; 
unsigned long debounceDelay = 50;    
const int buttonPin= 3;
int buttonState= {LOW};             
            int lastButtonState = {LOW};
            int reading;


const int MPU_addr=0x68;
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
int minVal=265;
int maxVal=402;
double x,y,z;


int flexSensorPin0 = A0; //analog pin 0
int flexSensorPin1 = A1; //analog pin 1
int flexSensorPin2 = A2; //analog pin 0
int flexSensorPin3 = A3; //analog pin 1
int flexSensorPin4 = A4; //analog pin 0
int flexSensorPin5 = A5; //analog pin 1
int flexSensorPin6 = A6; //analog pin 0
int flexSensorPin7 = A7; //analog pin 1

void setup(){
Wire.begin(); Wire.beginTransmission(MPU_addr); 
Wire.write(0x6B); Wire.write(0);
Wire.endTransmission(true);
pinMode(pushButton, INPUT);
pinMode(buttonPin, INPUT);
Serial.begin(9600);
}
void loop(){
Wire.beginTransmission(MPU_addr);
Wire.write(0x3B); 
Wire.endTransmission(false);
Wire.requestFrom(MPU_addr,14,true);
AcX=Wire.read()<<8|Wire.read();
AcY=Wire.read()<<8|Wire.read(); 
AcZ=Wire.read()<<8|Wire.read(); 
GyX=Wire.read()<<8|Wire.read();
GyY=Wire.read()<<8|Wire.read(); 
GyZ=Wire.read()<<8|Wire.read(); 
int xAng = map(AcX,minVal,maxVal,-90,90);
int yAng = map(AcY,minVal,maxVal,-90,90); 
int zAng = map(AcZ,minVal,maxVal,-90,90);
int buttonState1 = digitalRead(pushButton);


x= RAD_TO_DEG * (atan2(-yAng, -zAng)+PI); 
y= RAD_TO_DEG * (atan2(-xAng, -zAng)+PI); 
z= RAD_TO_DEG * (atan2(-yAng, -xAng)+PI);

if(x>=180&&x<360){
  x=-(360-x);
}

if(y>=180&&y<360){
  y=-(360-y);
}

if(z>=180&&z<360){
  z=-(360-z);
}
  
int flexSensorReading0 = analogRead(flexSensorPin0);
int flexSensorReading1 = analogRead(flexSensorPin1);
int flexSensorReading2 = analogRead(flexSensorPin2);
int flexSensorReading3 = analogRead(flexSensorPin3);
int flexSensorReading4 = analogRead(flexSensorPin4);
int flexSensorReading5 = analogRead(flexSensorPin5);
int flexSensorReading6 = analogRead(flexSensorPin6);
//int flexSensorReading7 = analogRead(flexSensorPin7);
//int flex0to1000 = map(flexSensorReading0, 280, 430, 0, 100);
//int flex0to1001 = map(flexSensorReading1, 180, 300, 0, 100);
{
   reading= digitalRead(buttonPin);       
  if (reading != lastButtonState)
      {
         lastDebounceTime = millis();
       }
  if ((millis() - lastDebounceTime) > debounceDelay)
  {
          
    if (reading != buttonState) 
   {  
      buttonState= reading;          
      if (buttonState == HIGH) 
       {                              
          Serial.print('\n');   
        }         
           }
  }
lastButtonState= reading;                      
}
if(buttonState1==0){
Serial.print(flexSensorReading0);
Serial.print('\t');
Serial.print(flexSensorReading1);
Serial.print('\t');
Serial.print(flexSensorReading2);
Serial.print('\t');
Serial.print(flexSensorReading3);
Serial.print('\t');
Serial.print(flexSensorReading4);
Serial.print('\t');
Serial.print(flexSensorReading5);
Serial.print('\t');
Serial.print(flexSensorReading6);
Serial.print('\t');
//Serial.print(flexSensorReading7);
//Serial.print('\t');
Serial.print(x);
Serial.print('\t');
Serial.print(y);
Serial.print('\t');
Serial.println(z);
/*Serial.print('\t');
Serial.print(AcX);
Serial.print('\t');
Serial.print(AcY);
Serial.print('\t');
Serial.println(AcZ);
/*Serial.print('\t');
Serial.print(GyX);
Serial.print('\t');
Serial.print(GyY);
Serial.print('\t');
Serial.println(GyZ);*/

}



//Serial.print(flexSensorReading1);
//Serial.print('\t');
//Serial.println(flex0to1001);

}







