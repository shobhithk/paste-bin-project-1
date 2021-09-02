from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4



app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sqlite3'
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    uid=db.Column(db.String(1000))
    text= db.Column(db.String(1000))


    def __init__(self, uid, text):
        self.uid = uid
        self.text = text



@app.route('/')
def text():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def text_post():
    text = request.form['name']
    uid = str(uuid4())
    newData = Data(uid, text)
    db.session.add(newData)
    db.session.commit()
    processed_text = text

    return f'<h1>{processed_text}</h1>'



@app.route("/view")
def view():
    return render_template('view.html',values=Data.query.all())

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)







