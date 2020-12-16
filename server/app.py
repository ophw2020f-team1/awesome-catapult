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
    return "success"


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
