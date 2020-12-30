  #include <Wire.h>
  #include <SoftwareSerial.h>

  SoftwareSerial mySerialx(6, 7);
  SoftwareSerial mySerialy(8, 9);
  SoftwareSerial mySerialz(10, 11);
  
  int count;


  long previousMillis = 0;        // will store last time LED was updated
   
  // the follow variables is a long because the time, measured in miliseconds,
  // will quickly become a bigger number than can be stored in an int.
  long interval = 10;           // interval at which to blink (milliseconds)

  void setup() {
    Serial.begin(9600);
    //Wire.begin();
    mySerialx.begin(9600);
    mySerialy.begin(9600);
    mySerialz.begin(9600);
    pinMode(6, INPUT);
    pinMode(7, OUTPUT);
    pinMode(8, INPUT);
    pinMode(9, OUTPUT);
  
    while(!Serial){
      
    }
  
  }
  
  void loop() {
    //Wire.requestFrom(10, 1);    // request 6 bytes from slave device #2
    
    
    mySerialx.listen();
    unsigned long currentMillis = millis();
    while( currentMillis - previousMillis > interval)
    {
       if(mySerialx.available() > 1)
        {
          int v1 = mySerialx.read();
          int v2 = mySerialx.read();
          Serial.print("X Position: ");
          Serial.print(v1);
          Serial.print(" ");
          Serial.println(v2);
        }
    }
   
    
     
    mySerialy.listen();
    currentMillis = millis();
    while( currentMillis - previousMillis > interval)
    {
       if(mySerialy.available() > 1)
        {
          int v1 = mySerialy.read();
          int v2 = mySerialy.read();
          Serial.print("Y Position: ");
          Serial.print(v1);
          Serial.print(" ");
          Serial.println(v2);
        }
    }
   
  //  mySerialz.listen();
  //  if(mySerialz.available() > 1)
  //   {
  //      int v1 = mySerialz.read();
  //      int v2 = mySerialz.read();
  //      Serial.print("Z Position: ");
  //      Serial.print(v1);
  //      Serial.print(" ");
  //      Serial.println(v2);
  //   }
  //    
  }
