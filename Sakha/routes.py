from flask import render_template, url_for, redirect, flash, request
from flask_mail import Message
from flask_login import login_user, logout_user, current_user, login_required
from Sakha import app, db, mail, bcrypt
from Sakha.form import LoginForm, RegistrationForm
from Sakha.models import User






@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')


@app.route('/about_us')
def about_us():
    return render_template('aboutus.html', title='About Us')



def registration_mail(user):
    msg = Message('Registration Successful', sender=('Team Sakha',app.config['MAIL_USERNAME']), recipients=[user.email])
    msg.html = f'''<h1>🎊 Congratulation {user.firstname + ' ' + user.lastname}</h1>
<p>You have created a brand new account in our platform and we are glad to get you as a new user and welcome you on </b>Sakha</b>.</p>
<p>You can login using the <a href="http://127.0.0.1:5000/login" target="_blank" rel="noreferrer noopener">link</a>.</p>'''
    mail.send(msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data,
                    email=form.email.data ,gender=form.gender.data, password = hashed_pw)
        db.session.add(user)
        db.session.commit()
        # registration_mail(user)
        flash('You have created a brand new account', 'info')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Here', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            flash(f'Welcome back {user.firstname}, you are logged in', 'info')
            return redirect(next) if next else redirect(url_for('home'))
        else:
            flash('Either username or password is wrong', 'warning')
    return render_template('login.html', title='Login Here', form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out', 'info')
    return redirect(url_for('home'))