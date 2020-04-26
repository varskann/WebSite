from flask import Flask, render_template
from forms import ContactForm
from flask import request

import os

app = Flask(__name__)

app.secret_key = b'\xb5\xfb\xc3\x16a\x7f\xd4\xe2\xa6!\x13\x7f\xa8\xbf@oo\xfbY$\xc7\x1cy '

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

    app.run()