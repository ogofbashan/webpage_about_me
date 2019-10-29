from app import app
from flask import render_template
from app. models import Project


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home',)
