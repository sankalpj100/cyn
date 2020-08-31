from flask import Flask, render_template, request
from p import cyn
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/happynews')
def h():
	return render_template(cyn(1))

@app.route('/sadnews')
def s():
	# cyn(2)
	return render_template(cyn(2))

@app.route('/allnews')
def a():
	# cyn(3)
	return render_template(cyn(3))

if __name__ == '__main__':
	app.debug = True
	app.run()