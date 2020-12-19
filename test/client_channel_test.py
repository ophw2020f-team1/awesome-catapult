import os
import time
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

mode = 2

def handleChannelMessage():
    msg = clientChannel.read()
    if msg == '':
        return
    if msg == 'a':
        mode = 2
        print(mode)
    elif msg == 'v':
        mode = 3
        print(mode)
    elif msg == 'm':
        mode = 1
        print(mode)
    elif msg == 'z':
        print('z')
        # a.send('z')
    else:
        print(msg)
        # a.send(msg)
    clientChannel.write('')

while True:
    handleChannelMessage()
    time.sleep(1)