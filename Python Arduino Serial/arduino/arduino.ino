//We want to receive the value  in  $050255 ($,050,255)
#define numofValsRec 2    // receiving 2 value
#define digitsPerValRec 3  // receiving 3 digit for each value

int valsRec[numofValsRec]; // create array of data store from receive
int stringLength = numofValsRec * digitsPerValRec + 1; // length of the value total
int counter = 0;
bool counterStart = false;
String receivedString;
void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}
void receiveData() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '$') {
      counterStart = true;
    }
    if (counterStart) {
      if (counter < stringLength) {
        receivedString = String(receivedString + c);
        counter++;
      }
      if (counter >= stringLength) {
        for (int i = 0; i < numofValsRec; i++) {
          int num = (i * digitsPerValRec) + 1;
          valsRec[i] = receivedString.substring(num, num + digitsPerValRec).toInt();
        }
        receivedString = "";
        counter = 0;
        counterStart = false;
      }
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  receiveData();
  // Input in serial monitor $027000 to turn led on
  //  if (valsRec[0] == 27) {
  //    digitalWrite(13, HIGH);
  //  }
  if (valsRec[1] == 255) {
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }

}
