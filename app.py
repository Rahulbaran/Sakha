from flask import Flask, render_template, url_for, request, abort, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user , login_required, current_user
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail




app = Flask(__name__)





@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')



@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', title='Register Here')



@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login Here')






if __name__=="__main__":
    app.run(debug=True, port=6433)