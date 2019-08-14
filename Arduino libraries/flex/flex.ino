int flexSensorPin0 = A0; //analog pin 0
int flexSensorPin1 = A1; //analog pin 1
int flexSensorPin2 = A2; //analog pin 0
int flexSensorPin3 = A3; //analog pin 1
int flexSensorPin4 = A4; //analog pin 0
int flexSensorPin5 = A5; //analog pin 1
int flexSensorPin6 = A6; //analog pin 0
int flexSensorPin7 = A7; //analog pin 1

void setup(){
Serial.begin(9600);
}

void loop(){
int flexSensorReading0 = analogRead(flexSensorPin0);
int flexSensorReading1 = analogRead(flexSensorPin1);
int flexSensorReading2 = analogRead(flexSensorPin2);
int flexSensorReading3 = analogRead(flexSensorPin3);
int flexSensorReading4 = analogRead(flexSensorPin4);
int flexSensorReading5 = analogRead(flexSensorPin5);
int flexSensorReading6 = analogRead(flexSensorPin6);
int flexSensorReading7 = analogRead(flexSensorPin7);
//int flex0to1000 = map(flexSensorReading0, 280, 430, 0, 100);
//int flex0to1001 = map(flexSensorReading1, 180, 300, 0, 100);
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
Serial.println(flexSensorReading7);


//Serial.print(flexSensorReading1);
//Serial.print('\t');
//Serial.println(flex0to1001);

//delay(250); //just here to slow down the output for easier reading
}
