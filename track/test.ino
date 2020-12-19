#include<Servo.h>

Servo servo_2; 
Servo servo_3;
Servo servo_4; //base
Servo servo_5;
String temp = "";
char c;
int angle[2] = {0}, mark = 0;

void setup(){
  Serial.begin(9600);
  servo_2.attach(2);
  servo_4.attach(4);
  servo_3.attach(3);
  servo_5.attach(5);  
}

void loop(){

  int j = 0;
  while (Serial.available() > 0){
    c = char(Serial.read());
    if(c == 'f') break;
    temp += c;
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
      servo_4.write(90);
      Serial.println(angle[0]);
      Serial.println(angle[1]);
      delay(1000);
      if(
      servo_5.write(angle[1]);
      delay(100);
      
      angle[0] = 0;
      angle[1] = 0;

}
}
