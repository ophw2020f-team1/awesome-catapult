#include <Servo.h>

Servo servo_2;
void direction() {
  servo_2.write(45);
  delay(50);
}

long item;
Servo servo_4;
void distance() {
  servo_4.write(90);
  delay(2000);
}

Servo servo_3;
void base() {
  servo_3.write(0);
  delay(50);
  servo_3.write(90);
  delay(50);
}

Servo servo_5;
void shoot() {
  servo_5.write(0);
  delay(100);
}

void reset() {
  servo_2.write(90);
  delay(0);
  servo_4.write(0);
  delay(500);
  servo_5.write(90);
  delay(0);
}

void setup()
{
  Serial.begin(9600);
  item = 'z';
  servo_2.attach(2);
  servo_4.attach(4);
  servo_3.attach(3);
  servo_5.attach(5);
}

void loop()
{
  reset();
  if (Serial.available() > 0) {
    item = Serial.read();
    if (item == 'a') {
      direction();
      base();
      distance();
      shoot();

    }

  } else {
    reset();

  }

}
