from flask import Flask, request, session 
from flask import render_template

import random

app = Flask(__name__)
app.secret_key = b'pickle' #my key

#- Multiple routes (at least 2)

#Use flask templates with substitutions

# At least one example of using the flask session.

@app.route("/")
def homePage():
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1
  return render_template("home.html",count = session['count'])

@app.route("/about")
def about():
  return render_template("about.html")
  
@app.route("/form",methods=['GET','POST'])
def form():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("form.html")
  else:
    # here we clicked the button
    # so we can check the form data
    email = request.form['email']
    comments = request.form['comments']
    print(email,comments)
    return "<h1>Your comment has been received. Here's what you entered: </h1><br>"+email+comments;

  
app.run(host="0.0.0.0",port=5000,debug=True)