int tempnr = 2;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(19200);
}

void writeint() {
    int value = analogRead(tempnr);
    Serial.write(highByte(value));
    Serial.write(lowByte(value));
 }

void loop() {  
  writeint();
  delay(1000);
}
