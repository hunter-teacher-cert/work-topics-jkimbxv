#followed tutorial https://www.youtube.com/watch?v=Z1RJmh_OqeA
from flask import Flask, render_template,url_for, request  #imports flask library
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) #app refers this file
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db' #importing databases
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200),nullable=False) #how many characters for task, can the task be blank? # NOTE:
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id #returns task string and id of that task


@app.route('/', methods=['POST','GET'])#what does setting a route do?
def index():
    if request.method == 'POST':
        task_content = request.form['content'] #passes in id of form from index.html
        new_task = Todo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'issue adding task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True) #any errors will pop up on main page

#html files can be inherited so you don't have to rewrite all the gobbledygook of html
#set up virtual env in terminal
#python3
#from app import db
#db.create_all()
#exit()
