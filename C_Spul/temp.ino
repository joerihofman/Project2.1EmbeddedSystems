int tempnr=0;
int lightnr=2;

void setup() {
  Serial.begin(19200); //baud rate.
}

void loop() {
  int var = Serial.read();
    
  switch(var) {
  case 1:
  temp();
  break;
  case 2:
  light();
  break;
  case 3:
  Serial.write(9);
  break;
  }
}

void light() {
  int waarde = analogRead(lightnr);
  Serial.write(1);
  delay(50);
  Serial.write(waarde);
 }

void temp() {
  int waarde = analogRead(tempnr);
  Serial.write(2);
  delay(50);
  Serial.write(waarde);
}

void lamp() {
  
}
