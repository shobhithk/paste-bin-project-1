from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.sqlite3'
db = SQLAlchemy(app)


class data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(100))
    text = db.Column(db.String(1000))

    def __init__(self, uid, text):
        self.uid = uid
        self.text = text


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        text = request.form['name']
        uid = str(uuid4())
        newData = data(uid, text)
        db.session.add(newData)
        db.session.commit()
        return redirect(url_for("user", usr=uid))
    else:
        return render_template('index.html')


@app.route("/<usr>")
def user(usr):
    found_user = data.query.filter_by(id=usr).first()
    return f'<h1>{found_user.text}</h1>'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)




