int soundSensor = A0;    // select the input pin for the potentiometer
int rledPin = A1;
int gledPin = A2;
int bledPin = A3;  // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor
const long interval = 500;
unsigned long previousMillis = 0;

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(rledPin, OUTPUT);
  pinMode(gledPin, OUTPUT);  
  pinMode(bledPin, OUTPUT);
  pinMode(soundSensor, INPUT);  

}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(soundSensor);    
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;

    if (sensorValue > 700){
      // turn the ledPin on
      analogWrite(rledPin, 51);
      analogWrite(gledPin, 255);
      analogWrite(bledPin, 20);
    }
    else{
      analogWrite(rledPin, 0);
      analogWrite(gledPin, 0);
      analogWrite(bledPin, 0);
    }
  }             
}
