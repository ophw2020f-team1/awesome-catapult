from moocxing.package import MOOCXING
from moocxing.robot.Brain import Brain

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

serial = mx.initSerial(com="COM4", bps=9600)

speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)

print("************initialization finish**********")

brain = Brain({"media": media, "speech": speech, "serial":serial})

print("************技能插件加载完毕**********")

def TTSPlay(text):
    speech.TTS(text)
    media.play()

def recordSTT():
    media.record()
    return speech.STT()

while True:
    result = recordSTT()
    thatangle = ''
    #请说 发射
    if not brain.query(result, _print=True):
        if "发射" in result:
            TTSPlay("好的，即将发射")
            serial.send(thatangle)

