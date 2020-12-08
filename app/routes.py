from app import app
from flask import url_for, redirect

@app.route('/')
@app.route('/index/')
def index():
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, Betty!</h1>
        <img src="static/ded905929f9f27d5e6f084b799f4c8f1d145ec72.jpg" align="middle" />
    </body>
</html>'''
# @app.route('/display/<filename>')
# def display_image(filename):
# 	#print('display_image filename: ' + filename)
# 	return redirect(url_for('static', filename='uploads/' + filename), code=301)
# THIS DOESNT WORK <img src="{{ url_for('static', filename='ded905929f9f27d5e6f084b799f4c8f1d145ec72.jpg') }}" align="middle" />
