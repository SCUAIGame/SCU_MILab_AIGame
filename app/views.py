from flask import render_template
from app import app

@app.route('/index')
@app.route('/index.html')
def index():
 return render_template("index.html")

@app.route('/about_us.html')
def about_us():
 return render_template("about_us.html")

@app.route('/contact.html')
def contact():
 return render_template("contact.html")
