from flask import Flask
import flask
import os

app = Flask(__name__)

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

@app.route('/')
def index():
    return flask.render_template('./index.html')


@app.route('/shoot', methods=['POST'])
def shoot():
    app.logger.info('shoot')
    serverChannel.write('z')

    return "success"


@app.route('/angle/<base>/<gear>', methods=['POST'])
def angle(base, gear):
    app.logger.info(f'angle: {base},{gear}')
    msg = f'{base},{gear}'
    serverChannel.write(msg)

    return 'success'


@app.route('/mode/<value>', methods=['POST'])
def mode(value):
    app.logger.info('mode: ' + value)
    value = value[:1]
    serverChannel.write(value)

    return "success"


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
