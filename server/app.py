from flask import Flask
import flask
import serial

# todo: 取消注释
# ser = serial.Serial('COM3')  # 按实际改

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('./index.html')


@app.route('/voice', methods=['POST'])
def voice():
    app.logger.info(flask.request.data)
    return 'success'


@app.route('/track', methods=['POST'])
def track():
    app.logger.info(flask.request.data)
    return 'success'


@app.route('/shoot', methods=['POST'])
def shoot():
    app.logger.info('shoot')
    # 向串口发送发射命令
    app.logger.info('serial: l')
    # todo: 取消注释
    # ser.write('l'.encode())

    return "success"


@app.route('/angle/<base>/<gear>', methods=['POST'])
def angle(base, gear):
    app.logger.info(f'angle: {base},{gear}')
    # 向串口发送改变角度指令
    msg = base + ',' + gear
    app.logger.info('serial: ' + msg)
    # todo: 取消注释
    # ser.write(msg.encode())

    return 'success'


@app.route('/mode/<value>', methods=['POST'])
def mode(value):
    app.logger.info('mode: ' + value)
    # 向串口发送改变模式命令
    msg = value[:1]
    app.logger.info('serial: ' + msg)
    # ser.write(msg.encode())

    return "success"


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
