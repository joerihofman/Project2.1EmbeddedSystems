void loop() {
  test();
}

 void test() {
  int analoogpoort=0;
  int waarde = analogRead(analoogpoort);
  Serial.write(1);
  delay(50);
  Serial.write(waarde);
 }
