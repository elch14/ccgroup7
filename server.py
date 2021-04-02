from flask import Flask,render_template, url_for, flash, redirect, request,session,make_response, jsonify, json
import requests
from flask_sqlalchemy import SQLAlchemy,sqlalchemy
from flask_bcrypt import Bcrypt
import json




"""
aws server
"""

app = Flask(__name__)
#secret key required for session, 
app.config['SECRET_KEY'] = '68371da38c85a1cedfe224853859e396'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

covid_main_url = 'https://api.covid19api.com/'


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    pass_hash = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '' % self.username

def create_db():
    db.create_all()


"""
Allows users to sign up with Username and password.
Takes the inputed password of the users and hashes the password into the database.
Stores username and only hashed password in the database
"""
@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        con_password = request.form['con_password']


        if not (username and password):
            flash("Username or Password cannot be empty")
            return redirect(url_for('signup'))
        elif (password != con_password):
            flash("Both passwords must be the same")
            return redirect(url_for('signup'))            
        else:
            username = username.strip()
            password = password.strip()

		#generates a hashed pasword with a salted key using bcrypt 
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')


        new_user = User(username=username, pass_hash=hashed_password)
        db.session.add(new_user)
        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            flash("Username {u} is not available.".format(u=username))
            return redirect(url_for('signup'))

        flash('Your account has been created! You are now able to log in')
        return redirect(url_for("login"))
    return render_template("register.html",title='Register')



"""
A summary of new and total cases per country updated daily. The home page for logged
in users.
"""
@app.route("/home/<username>")
def home(username):
    return render_template('home.html',username=username)




@app.route("/home/<username>/countries")
def home_countries(username):
    summary_url = covid_main_url + str('countries')
    resp = requests.get(summary_url)
    
    if resp.ok:
        summary_json = resp.json()
    else:
        print(resp.reasone)
    
    return jsonify(summary_json), 200
    return render_template('home.html',username=username)

@app.route("/home/<username>/summary")
def home_summary(username):
    summary_url = covid_main_url + str('summary')
    resp = requests.get(summary_url)
    
    if resp.ok:
        summary_json = resp.json()
    else:
        print(resp.reasone)
    
    return jsonify(summary_json), 200
    return render_template('home.html',username=username)


@app.route("/home/<username>/country/<name>", methods=['GET'])
def home_country(username,name):
    summary_url = covid_main_url + str('dayone/country/') + name
    resp = requests.get(summary_url)
    if resp.ok:
         summary_json = resp.json()
    else:
        print(resp.reasone)
    return jsonify(summary_json), 200
    return render_template('home.html',username=username)

    """
    Uses get request to allow users to login default as soon as enters the webpage.
    On post checks password hash from db for given input username and password.
    checks if both username and hash password match thaose in database. If matches
    redirects user to home page. If it doesnt match it sends a login error.
    """
@app.route("/")
@app.route("/login/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash("Both Username and Password must be filled in.")
            return redirect(url_for('login'))
        else:
            username = username.strip()
            password = password.strip()

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.pass_hash, password):
            session[username] = True
            return redirect(url_for("home", username=username))
        else:
            flash('Login Unsuccessful. Please check email and password')

    return render_template("login.html",title='Login')


"""
Logs users out and redirects them to the login page.
"""
@app.route("/logout/<username>")
def logout(username):
    session.pop(username, None)
    flash("successfully logged out.")
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Loads the SSL certificate for implementing HTTPS
    # app.run(debug=True,ssl_context=('cert.pem', 'key.pem'))
    app.run(debug=True,ssl_context=('cert.pem', 'key.pem'))
