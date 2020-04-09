from flask import Flask, render_template
from forms import ContactForm
from flask import request

import os

app = Flask(__name__)

app.secret_key = 'development key'

@app.route('/', methods=["GET", "POST"])
def index():
	form = ContactForm()

	images_path = "static/carousel"
	images = os.listdir(images_path)
 
	if request.method == 'POST':
		print(form.name)
 
	return render_template('index.html', form=form, images=images)

# @app.route("/gallery")
# def gallery():
# 	images_path = "static/carousel"

# 	images = os.listdir(images_path)
# 	print(images)
# 	return render_template('gallery.html', images=images)

if __name__ == '__main__':

    app.run(host='0.0. 0.0', debug=True)