#include<Servo.h>

Servo servo_2; 
Servo servo_3;
Servo servo_4; //base
Servo servo_5;
String temp = "";
char c;
int angle[2] = {0}, mark = 0;
bool shoot=false;
bool repeat=true;
void setup(){
  Serial.begin(9600);
  servo_2.attach(2);
  servo_4.attach(4);
  servo_3.attach(3);
  servo_5.attach(5);
  reset();
}

void loop(){
  int j = 0;
  while (Serial.available() > 0){
    c = char(Serial.read());
    if(c == 'f') break;
    if(c == 'z'){
      shoot = true;
      
      break;
    }
    temp += c;
    delay(2);
    mark = 1;
    }
  if(shoot) repeat = !repeat;
  if(shoot && repeat == false){
    Shoot();
    shoot = false;
    reset();
  }
  else{
    temp.replace("\n","") ;
    if(mark == 1) {
    //Serial.println(temp);
    //Serial.println(temp.length());
        for(int i=0;i<temp.length();i++){
          if(temp[i]==',' ){
            j++;
            }
          else{
            angle[j]=angle[j]*10+(temp[i]-'0');}
        }
        mark=0;
        temp=String("");
    
        servo_2.write(180);
        delay(50);
        servo_4.write(angle[0]);
        Serial.println(angle[0]);
        delay(1000);
        servo_5.write(90);
        delay(100);
        angle[0] = 0;
        angle[1] = 0;
      }
  }
}

void Shoot(){
  servo_2.write(60);
  delay(1000);
  servo_5.write(0);
}

void reset(){
  servo_4.write(90);
  servo_2.write(180);
  delay(1000);
  servo_5.write(90);
}

void load(){
  servo_3.write(0);
  delay(50);
  servo_3.write(90);
  delay(50);
}
