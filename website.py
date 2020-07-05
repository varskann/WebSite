from flask import Flask, render_template
from flask import request

import os, glob

app = Flask(__name__)

app.secret_key = b'\xb5\xfb\xc3\x16a\x7f\xd4\xe2\xa6!\x13\x7f\xa8\xbf@oo\xfbY$\xc7\x1cy '

@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('home.html')

@app.route("/gallery")
def gallery():
	images = glob.glob("static/carousel/*.*g") 
	images = [image.replace("\\", "/").replace("static", "..") for image in images]
	return render_template('gallery.html', images=images)

@app.route("/portfolio")
def portfolio():
	return render_template('portfolio.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

if __name__ == '__main__':

    app.run()