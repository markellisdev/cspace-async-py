from app import app
from flask import url_for, redirect, send_from_directory, render_template
import os

@app.route('/')
@app.route('/index', strict_slashes=False)
def index():
    image_names = os.listdir('app/static/')
    print(image_names)
    return render_template("display.html", len = len(image_names), image_names = image_names)