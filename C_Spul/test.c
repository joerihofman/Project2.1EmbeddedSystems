void tempvalue() {        
 int waarde = analogRead(analoogpoort);
 Serial.write(1);
 delay(50);
 Serial.write(waarde);
}
