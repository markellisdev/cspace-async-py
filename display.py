from app import app
from flask import url_for, redirect, send_from_directory, render_template
import os

@app.route('/')
@app.route('/index', strict_slashes=False)
def index():
    image_names = os.listdir('./imageStore')
    print(image_names)
    return render_template("display.html")