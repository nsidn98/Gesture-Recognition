void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}
float f0,f1, f2, f3, f4;
void loop() {
  // put your main code here, to run repeatedly:
  f0 = analogRead(0);
  f1 = analogRead(1);
  f2 = analogRead(2);
  f3 = analogRead(3);
  f4 = analogRead(4);
  Serial.print(f0);
  Serial.print('\t');
  Serial.print(f1);
  Serial.print('\t');
  /*Serial.print(f2);
  Serial.print('\t');*/
  Serial.print(f3);
  Serial.print('\t');
  Serial.println(f4);


}
