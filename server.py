from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self,username,password):
        self.username=username
        self.password=password


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(100))
    text = db.Column(db.String(1000))

    def __init__(self, uid, text):
        self.uid = uid
        self.text = text


@app.route('/')
def home_redirect():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            userdata = User.query.filter_by(username=username).first()
            if userdata.password == password:
                return redirect(url_for("home", username=username))
            else:
                return render_template('login.html')
        else:
            newData = User(username, password)
            db.session.add(newData)
            db.session.commit()
            return redirect(url_for("home", username=username))
    else:
        return render_template('login.html')


@app.route('/index.html/<username>', methods=['GET', 'POST'])
def home(username):
    if request.method == "POST":
        text = request.form['name']
        uid = str(uuid4())
        new_data = Data(uid, text)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for("user", usr=username,uid=uid))
    elif request.method == 'GET':
        return render_template('/index.html')
    else:
        return redirect(url_for("home", username=username))


@app.route("/<usr>/<uid>")
def user(usr, uid):
    found_user = Data.query.filter_by(uid=usr).first()
    return f'<h1>{found_user.text}</h1>'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)




