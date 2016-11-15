int tempnr=0;
int lightnr=2;
int led_groen=8;
int led_geel=9;
int led_rood=10;
int cm_uitrol=5;
int statusuit=3;
int var;
//Hier voeren we de variabele waardes in.

void setup() {
  Serial.begin(19200); //baud rate.
  pinMode(led_groen,OUTPUT);        //stelt de lampjes in.
  pinMode(led_geel,OUTPUT);
  pinMode(led_rood,OUTPUT);
  digitalWrite(led_groen,HIGH);     //we starten met een opgerold scherm
  }                                 //hier laten we groen voor branden

void loop() {
  if(Serial.available()){
  var = Serial.read();      //hier wordt de waarde gelezen die door python wordt gestuurd.
  kees(var);
  }                         //Daar moet arduino wat mee doen.
}

void kees(int var) {
  switch(var) {
  case '1': light();        break;  //Aantal lux opvragen
  case '2': temp();         break;  //Temp opvragen
  case '3': up();           break;  //De functie om scherm op te laten rollen
  case '4': down();         break;  //De functie om scherm naar beneden te laten rollen
  case '5': statusin();     break;  //Geeft de status van het scherm. Of die naar beneden of boven is
  case '6': ping();         break;  //Dit kijkt of het bordje kan communiceren. (soort whoami)
  case '7': uitrol(5);      break;  //Dit zet de uitrol op 50cm
  case '8': uitrol(10);     break;  //Dit zet de uitrol op 100cm
  case '9': uitrol(15);     break;  //Dit zet de uitrol op 150cm
  case '0': statusuitrol(); break;  //Dit geeft aan op hoeveel cm de scherm is uitgerold
  }
}

void light() {
  int waarde = analogRead(lightnr);
  Serial.write(highByte(waarde));
  Serial.write(lowByte(waarde));
 }

void temp() {
  int waarde = analogRead(tempnr);
  Serial.write(waarde);
}

void up() {
  digitalWrite(led_rood,HIGH);
  for (int x=0;x<cm_uitrol;x++) {          //zie commentaar void down (hieronder)
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
  statusuit = 3;
  Serial.write(3);
}

void down() {
  digitalWrite(led_groen,HIGH);
  for (int x=0;x<cm_uitrol;x++) {   //dit is als teller
    digitalWrite(led_geel,HIGH);    //de gele led laten we knipperen
    delay(500);                     //door modulo te gebruiken knippert de led
    if (x%2==0) {
      digitalWrite(led_geel,LOW);
      delay(500);
    }
  }
  digitalWrite(led_geel,LOW);
  digitalWrite(led_rood,HIGH);
  digitalWrite(led_groen,LOW);      //hier worden de leds goed gezet
  statusuit = 4;                    //dit is voor de status
  Serial.write(4);
}

void statusin() {
  Serial.write(statusuit);
}

void ping() {
  Serial.write(6);
}

void uitrol(int snelheid){
  cm_uitrol = snelheid;
  Serial.write(8);
}

void statusuitrol() {
  Serial.write(cm_uitrol);
}