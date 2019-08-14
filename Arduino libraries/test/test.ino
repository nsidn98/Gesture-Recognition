unsigned long lastDebounceTime = {0}; 
unsigned long debounceDelay = 50;    
const int buttonPin= {2}; 

            int buttonState= {LOW};             
            int lastButtonState = {LOW};
            int reading;

void setup() 
{
  Serial.begin(9600);
  
   pinMode(buttonPin, INPUT);
         
}



void loop()

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
                              Serial.print(buttonState);
                             
                         }
                         
            
           }
  }

  
  digitalWrite(ledPin, ledState);
   
                          
                            

lastButtonState= reading;                      
 
  

}*/
