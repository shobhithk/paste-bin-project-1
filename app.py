from flask import Flask, request, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello_world'
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
    if "uid" in session:
        session.pop("uid",None)
        session.pop("usr", None)
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if "username" in session:
            session.pop('username')
        session['username'] = username
        if User.query.filter_by(username=username).first():
            userdata = User.query.filter_by(username=username).first()
            if userdata.password == password:
                if "uid" in session:
                    return redirect(url_for("user" ,usr=session['usr'],uid=session['uid']))
                else:
                    return redirect(url_for("home", username=username))
            else:
                return render_template('login.html')
        else:
            newData = User(username, password)
            db.session.add(newData)
            db.session.commit()
            if "uid" in session:
                return redirect(url_for("user" ,usr=session['usr'],uid=session['uid']))
            else:
                return redirect(url_for("home", username=username))
    else:
        return render_template('login.html')


@app.route('/<username>', methods=['GET', 'POST'])
def home(username):
    if request.method == "POST":
        text = request.form['textform']
        uid = str(uuid4())
        new_data = Data(uid, text)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for("user", usr=username,uid=uid))
        #return (url_for("user", usr=username,uid=uid))

    elif request.method == 'GET':
        return render_template('/index.html')
    else:
        return redirect(url_for("home", username=username))


@app.route("/<usr>/<uid>",methods=['GET','POST'])
def user(usr, uid):
    if "usr" in session:
        session.pop('usr', None)
        session.pop('uid', None)
    session['usr']=usr
    session['uid']=uid
    found_data = Data.query.filter_by(uid=uid).first()
    if request.method == "POST":
        if "username" in session:
            if session['username'] == usr:
                text = request.form['textform']
                found_data.text = text
                db.session.commit()
                return render_template('/index.html', content=found_data.text)
            else:
                return render_template('/text.html', content=found_data.text, message="*only user can edit this")
        else:
            return redirect(url_for("login"))
    else:
        return render_template('/text.html', content=found_data.text)


if __name__ == '__main__':
    db.create_all()
    app.run()




