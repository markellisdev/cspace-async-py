from app import app
from flask import url_for, redirect, send_from_directory, render_template
import os


# @app.route('/display/<filename>')
# def display_image(filename):
# 	#print('display_image filename: ' + filename)
# 	return redirect(url_for('static', filename='uploads/' + filename), code=301)
# THIS DOESNT WORK <img src="{{ url_for('static', filename='ded905929f9f27d5e6f084b799f4c8f1d145ec72.jpg') }}" align="middle" />
# @app.route('/static/<filename>')
# def send_image(filename):
#     return send_from_directory("./imageStore", filename)

# @app.route('/gallery', methods=['GET', 'POST'])
# def get_gallery():
#     image_names = os.listdir('./imageStore')
#     print(image_names)
#     return render_template("gallery.html", image_names=image_names)