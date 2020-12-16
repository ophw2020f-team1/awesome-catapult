#include<Servo.h>

Servo servo_2;
Servo servo_3;
Servo servo_4;
Servo servo_5;
String temp = "";
int angle[2] = {0}, mark = 0;

void setup(){
  Serial.begin(9600);
  servo_2.attach(2);
  servo_4.attach(4);
  servo_3.attach(3);
  servo_5.attach(5);  
}

void loop(){
  reset();
  int j = 0;
  while (Serial.available() > 0){
    temp+= char(Serial.read());
    delay(2);
    mark = 1;
    }
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

    servo_2.write(angle[0]);
    delay(50);
    base();
    servo_4.write(angle[1]);
    delay(2000);
    servo_5.write(0);
    delay(100);
    angle[0]=0;
    angle[1]=0;
}
}


void reset(){
  servo_2.write(90);
  servo_4.write(0);
  delay(500);
  servo_5.write(90);
}

void base(){
  servo_3.write(0);
  delay(50);
  servo_3.write(90);
  delay(50);
}
