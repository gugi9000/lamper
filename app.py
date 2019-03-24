from flask import Flask, flash, redirect, url_for, render_template
from backend import set_lamp_on, find_lamps

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    lamps = find_lamps()
    return render_template('index.html', lamps=lamps)


@app.route('/on/<lamp>')
def on(lamp):
    status = set_lamp_on(lamp, True)
    if status:
        flash(f"Lamp turned on!", 'success')
    else:
        flash(f"Toggle failed: {status}", 'error')
    return redirect(url_for('index'))


@app.route('/off/<lamp>')
def off(lamp):
    status = set_lamp_on(lamp, False)
    if status:
        flash(f"Lamp turned off!", 'success')
    else:
        flash(f"Toggle failed: {status}", 'error')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
