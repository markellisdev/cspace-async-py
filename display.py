from app import app
from flask import url_for, redirect, send_from_directory, render_template
import os

@app.route('/')
@app.route('/index', strict_slashes=False)
def index():
    image_names = os.listdir('app/static/full/')
    
    # have to append str to each item for dir in static
    # initializing append_str 
    append_str = 'full/'
    
    # Append suffix / prefix to strings in list
    image_names = [append_str + sub for sub in image_names] 
    print(image_names)

    # use display template and pass vars needed for jinja templating for loop
    return render_template("display.html", len = len(image_names), image_names = image_names)