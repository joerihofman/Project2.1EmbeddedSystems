int tempnr=0;
int lightnr=2;
int led_groen=10;
int led_geel=9;
int led_rood=8;
int vertraging=500;
int stati=0;
//Hier voeren we de variabele waardes in.

void setup() {
  Serial.begin(19200); //baud rate.
  pinMode(led_groen,OUTPUT);
  pinMode(led_geel,OUTPUT);
  pinMode(led_rood,OUTPUT);
  }

void loop() {
  int var = Serial.read();  //hier wordt de waarde gelezen die door python wordt gestuurd. 
                            //Daar moet arduino wat mee doen.
  var -=48;
  switch(var) {
  case 1:
  temp();  break;
  case 2:
  light();  break;
  case 3:
  up();  break;
  case 4:
  down();  break;
  case 5:
  stati(); break;
  case 6:
  ping(); break;
  
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

void up() {
  digitalWrite(led_rood,HIGH);
  for (int x=0;x<10;x++) {
    digitalWrite(led_geel,HIGH);
    delay(500);
    if (x%2==0) {
      digitalWrite(led_geel,LOW);
      delay(500);
    }
  }
  digitalWrite(led_geel,LOW);
  digitalWrite(led_rood,LOW);
  digitalWrite(led_groen,HIGH);
  stati = 0;
  Serial.write(3);
}

void down() {
  digitalWrite(led_groen,HIGH);
  for (int x=0;x<10;x++) {
    digitalWrite(led_geel,HIGH);
    delay(500);
    if (x%2==0) {
      digitalWrite(led_geel,LOW);
      delay(500);
    }
  }
  digitalWrite(led_geel,LOW);
  digitalWrite(led_rood,HIGH);
  digitalWrite(led_groen,LOW);
  stati = 1;                    //dit is voor de status
}

int ping() {
  return 6;  
}

int stati() {
  return stati;
}
