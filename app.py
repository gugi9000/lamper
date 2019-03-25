from flask import Flask, flash, redirect, url_for, render_template
from backend import set_lamp_on, find_lamps, find_groups, get_lamps_by_group

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    lamps = find_lamps()
    groups = find_groups()
    return render_template('index.html', lamps=lamps, groups=groups)


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


@app.route('/all/<state>')
def toggle_all(state):
    light = True if state == 'on' else False
    lamps = find_lamps()
    status = True
    for lamp in lamps:
        res = set_lamp_on(lamp[0], light)
        if not res:
            status = False

    if status:
        flash(f"All lamps toggled!", 'success')
    else:
        flash(f"Toggle failed!", 'error')
    return redirect(url_for('index'))


@app.route('/group/<state>/<group_id>')
def toggle_group(state, group_id):
    light = True if state == 'on' else False
    lamps = get_lamps_by_group(group_id)
    status = True
    for lamp in lamps:
        res = set_lamp_on(lamp, light)
        if not res:
            status = False

    if status:
        flash(f"All lamps toggled!", 'success')
    else:
        flash(f"Toggle failed!", 'error')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
