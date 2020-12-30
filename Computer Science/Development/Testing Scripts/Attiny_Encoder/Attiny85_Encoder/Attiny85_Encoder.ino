/* Bounce-Free Rotary Encoder

   David Johnson-Davies - www.technoblogy.com - 28th October 2017
   ATtiny85 @ 1 MHz (internal oscillator; BOD disabled)
   
   CC BY 4.0
   Licensed under a Creative Commons Attribution 4.0 International license: 
   http://creativecommons.org/licenses/by/4.0/
*/

unsigned long interval = 100; //Rate to send encoder pulses
unsigned long previousMillis = 0; //used for non-blocking timer

const int EncoderA = 3; //pin to read encoder A pulses (pin 2 on Attiny85)
const int EncoderB = 4; //pin to read encoder B pulses (pin 3 on Attiny85)

// Rotary encoder **********************************************

volatile int a0;
volatile int c0;
volatile int Count = 0; //regular integer to store value
volatile byte data[2]; //used to store the integer for serial sending

// Called when encoder value changes
void ChangeValue (bool Up) {
  Count = max(min((Count + (Up ? 1 : -1)), 1000), -1000);
}

// Pin change interrupt service routine
ISR (PCINT0_vect) {
  int a = PINB>>EncoderA & 1;
  int b = PINB>>EncoderB & 1;
  if (a != a0) {              // A changed
    a0 = a;
    if (b != c0) {
      c0 = b;
      ChangeValue(a == b);
    }
  }
}

// Setup demo **********************************************

void setup() {
  Serial.begin(9600); //TX is physical pin 5, RX pin 6
  pinMode(EncoderA, INPUT_PULLUP);
  pinMode(EncoderB, INPUT_PULLUP);
  PCMSK = 1<<EncoderA;        // Configure pin change interrupt on A
  GIMSK = 1<<PCIE;            // Enable interrupt
  GIFR = 1<<PCIF;             // Clear interrupt flag
}

void loop(){

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    data[0] = (byte) (Count & 0xFF); //bitmask the top half of the integer (bits 16 - 9)
    data[1] = (byte) ((Count >> 8) & 0xFF); //bitmask bottom half of integer (bits (8 - 1)
    Serial.write(data[0]); //Send lower byte first
    Serial.write(data[1]); //Send upper byte second
  }
  
}
