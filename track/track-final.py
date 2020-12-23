import numpy as np
import cv2
from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain
import time
import myserial as se
import os
import threading

com= se.comPorts(0)
a  = se.MXSerial(com,9600)
'''
while True:
    a.send(input("输入指令："))
    time.sleep(0.8)
       
a.close()
'''

mx = MOOCXING()
'''
APP_ID = '22929503'
API_KEY = 'WresMkF1o4342KeqZBOsjXId'
SECRET_KEY = 'BrDOj5quiTuhwxpULsVzWdw5nmcyrTIl'
'''
APP_ID='23084382'
API_KEY='ka5P4d1iP9W8yEsIcFwGPYCm'
SECRET_KEY='xQXk8YV5YYPhIvmG23eX21Wgp5E6m8h6'

media = mx.initMedia()

speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)

print("************initialization finish**********")

brain = Brain({"media": media, "speech": speech})

print("************技能插件加载完毕**********")

def TTSPlay(text):
    speech.TTS(text)
    media.play()

def recordSTT():
    media.record()
    return speech.STT()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

mode = 2

last = 0


class Channel:
    def __init__(self, channelPath) -> None:
        super().__init__()
        self.channelPath = channelPath


    def read(self):
        res = ''
        with open(self.channelPath, 'r') as file:
            res = file.read()
            return res


    def write(self, msg):
        with open(self.channelPath, 'w') as file:
            file.write(msg)

channelPath = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\\channel.txt') 
clientChannel = Channel(channelPath)

def handleChannelMessage():
    msg = clientChannel.read()
    global mode
    if msg == '':
        return
    if msg == 'a':
        print('a')
        mode = 2
    elif msg == 'v':
        print('v')
        mode = 3
    elif msg == 'm':
        print('m')
        mode = 1
    elif msg == 'z':
        print('z')
        a.send('z')
    else:
        print(msg)
        a.send(msg)
    clientChannel.write('')


def handleChannelThread():
    while True:
        # print('handleChannelThread')
        handleChannelMessage()
        time.sleep(0.2)


readChannelThread = threading.Thread(target=handleChannelThread, name='readChannelThread')
readChannelThread.start()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    img = frame #shape(480,640,3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    servo_positionx = 0
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(faces)
    for (x, y, w, h) in faces: # 如果有两张脸的话需要另外调试
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex, ey, ew, eh) in eyes:
            #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        #print("x:", (x + w / 2))
        servo_positionx = 2 * (x) / 480 - 1
        servo_positiony = 2 * (y + h / 2) / 640 - 1
    cv2.imshow('img', img)
    key = cv2.waitKey(200)
    if key == ord('q'):
        break
    if key == ord('k'): #手动模式
        mode = 1
    if key == ord('a'): #自动模式
        mode = 2
    if key == ord('v'): #语音模式
        mode = 3
    if(servo_positionx != 0 and mode == 2):
        print(str(int(-servo_positionx * 70 + 100)))
        #serial.send(str(int(servo_positionx * 60)))
        
        if(int(-servo_positionx * 70 + 100) - 5 <= last <= int(-servo_positionx * 70 + 100) + 5):
            a.send('z')
        else:
            a.send(str(int(-servo_positionx * 70 + 100)))

        last = int(-servo_positionx * 70 + 100)
        
        #msg = a.readline()
        #print("msg:",msg)
        time.sleep(1.2)
    if mode == 1:
        a.send(str(input("输入指令：")))
        #msg = a.readline()
        #print("msg:",msg)
        time.sleep(0.8)
    while mode == 3:
        result = recordSTT()
        # 请说 发射
        if not brain.query(result, _print=True):
            if "发射" in result:
                TTSPlay("好的，即将发射")
                a.send('z')
                time.sleep(0.5)
                a.send('z')
            if "自动" in result:
                TTSPlay("好的，切换成自动模式")
                mode = 2
                break
            if "手动" in result:
                TTSPlay("好的，切换成手动模式")
                mode = 1
                break


cv2.destroyAllWindows()
cap.release()
a.close()
