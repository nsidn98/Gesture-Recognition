int flexSensorPin0 = A0; //analog pin 0

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
int flexSensorReading0 = analogRead(flexSensorPin0);
Serial.println(flexSensorReading0);

}
