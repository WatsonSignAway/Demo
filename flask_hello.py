from flask import Flask
from flask import render_template


app = Flask("_name_")
@app.route('/Documents/IBM_Watson/')


def index(name=None):
	return render_template('index.html', name=name)

# Run these on terminal
# $ export FLASK_APP=flask_hello.py
# $ flask run
# * Running on http://127.0.0.1:5000/