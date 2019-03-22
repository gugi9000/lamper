from flask import Flask, render_template
from backend import set_lamp_on, find_lamps

app = Flask(__name__)


@app.route('/')
def index():
    lamps = find_lamps()
    return render_template('index.html', lamps=lamps)


@app.route('/on/<lamp>')
def on(lamp):
    status = set_lamp_on(lamp, True)
    return render_template('on.html', status=status)


@app.route('/off/<lamp>')
def off(lamp):
    status = set_lamp_on(lamp, False)
    return render_template('on.html', status=status)


if __name__ == '__main__':
    app.run()
