from flask import Flask
import flask

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
    # todo: 向串口发送发射命令

    return "success"


@app.route('/angle/<base>/<gear>', methods=['POST'])
def angle(base, gear):
    app.logger.info('angle:' + base + '   ' + gear)
    # todo: 向串口发送改变角度指令

    return 'success'


@app.route('/mode/<value>', methods=['POST'])
def mode(value):
    app.logger.info('mode: ' + value)
    # todo: 向串口发送改变模式命令

    return "success"


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
