from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

import numpy as np


app = Flask(__name__)


def picked_up():
    messages = ["Hello",
                "yoyo",
                "poyoyoyoyoyon"]
    return np.random.choice(messages)


@app.route('/')
def index():
    title = "welcome"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)


@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "KONNNICHIHA"
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html',
                               name=name, title=title)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
