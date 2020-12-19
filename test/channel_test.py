import os

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
serverChannel = Channel(channelPath)

while True:
    msg = serverChannel.read()
    if msg != '':
        print(msg)
        serverChannel.write('')
        if msg == 'q':
            break