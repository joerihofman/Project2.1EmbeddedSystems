int tempnr=0;
int lightnr=2;
int led_groen=8;
int led_geel=9;
int led_rood=10;
int vertraging=500;
int stati=3;
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
  kees(var);  
}

void kees(int var) {
//  var -=48;  
  switch(var) {
  case 1:
  light();  break;
  case 2:
  temp();  break;
  case 3:
  up();  break;
  case 4:
  down();  break;
  case 5:
  statu(); break;
  case 6:
  ping(); break;  
  }
}

void light() {
  int waarde = analogRead(lightnr);
  Serial.write(1);
  delay(50);   
  Serial.write(highByte(waarde));
  Serial.write(lowByte(waarde));
 }

void temp() {
  int waarde = analogRead(tempnr);
  Serial.write(2);
  delay(50);
  Serial.write(waarde);
}

void up() {
  digitalWrite(led_rood,HIGH);
  for (int x=0;x<10;x++) {          //zie commentaar void down
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
  stati = 3;
  Serial.write(3);
}

void down() {
  digitalWrite(led_groen,HIGH);
  for (int x=0;x<10;x++) {          //dit is als teller
    digitalWrite(led_geel,HIGH);    //de gele led laten we knipperen
    delay(500);                     //door modulo te gebruiken knippert de led
    if (x%2==0) {
      digitalWrite(led_geel,LOW);
      delay(500);
    }
  }
  digitalWrite(led_geel,LOW);
  digitalWrite(led_rood,HIGH);
  digitalWrite(led_groen,LOW);  //hier worden de leds goed gezet
  stati = 4;                    //dit is voor de status
  Serial.write(4);
}

void statu() {
  Serial.write(stati);
}

void ping() {
  Serial.write(6);  
}
