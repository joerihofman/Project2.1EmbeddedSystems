void setup() {
  Serial.begin(19200); //baud rate.
}

void loop() {
  int var = Serial.read();
  if (var == 1) {
    temp();
  }
}

void temp() {
  int analoogpoort=0;
  int waarde = analogRead(analoogpoort);
  Serial.write(1);
  delay(50);
  Serial.write(waarde);
 }
