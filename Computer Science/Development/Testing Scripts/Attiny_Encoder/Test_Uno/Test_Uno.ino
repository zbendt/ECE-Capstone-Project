#include <Wire.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3);

int count;

void setup() {
  Serial.begin(9600);
  //Wire.begin();
  mySerial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  while(!Serial){
    
  }

}

void loop() {
  //Wire.requestFrom(10, 1);    // request 6 bytes from slave device #2

  if(mySerial.available() > 1)
   {
      int v1 = mySerial.read();
      int v2 = mySerial.read();
      Serial.print(v1);
      Serial.print(" ");
      Serial.println(v2);
   }
    
}
