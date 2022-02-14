from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

#example of route that passes data to a render_template
@app.route("/rand")
def randomnumber():
    i = random.randrange(100)
    return render_template("lucky.html",number=i)

#the root route
@app.route("/")
def index():
    return "<h1>hello world from jiyoon</h1>"

@app.route("/about")
def about():
    return render_template("about.html")

app.run(host="0.0.0.0",port = 5000, debug=True)
