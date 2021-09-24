import secrets, os
from flask import render_template, url_for, redirect, flash, request
from flask_mail import Message
from flask_login import login_user, logout_user, current_user, login_required
from Sakha import app, db, mail, bcrypt
from Sakha.form import LoginForm, RegistrationForm, NameUpdateForm, AboutUpdateForm,\
                       UniqueDetailsUpdateForm, UploadAvatarForm
from Sakha.models import User






@app.route('/')
@app.route('/home')
def home():
    return render_template('sites/home.html', title = 'Home')



@app.route('/about_us')
def about_us():
    return render_template('sites/aboutus.html', title='About Us')



@app.route('/contact_us')
def contact_us():
    return render_template('sites/contact.html', title='Contact Us')



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
    return render_template('users/register.html', title='Register Here', form=form)



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
    return render_template('users/login.html', title='Login Here', form=form)




@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out', 'info')
    return redirect(url_for('home'))




@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    nameForm = NameUpdateForm()
    uniqueForm = UniqueDetailsUpdateForm()
    aboutForm = AboutUpdateForm()
    nameForm.firstname.data = current_user.firstname
    nameForm.lastname.data = current_user.lastname
    aboutForm.about_user.data = current_user.about_user
    aboutForm.address.data = current_user.address
    if request.method=="GET":
        uniqueForm.username.data = current_user.username
        uniqueForm.email.data = current_user.email
    if uniqueForm.validate_on_submit():
        current_user.username = uniqueForm.username.data
        current_user.email = uniqueForm.email.data
        db.session.commit()
        flash('Your account details has been updated', 'info')
        return redirect(url_for('settings'))
    return render_template('users/settings.html', title='Settings',nameForm=nameForm,\
                             aboutForm=aboutForm, uniqueForm=uniqueForm)




@app.route('/updateName',methods=['POST'])
@login_required
def updateName():
    data = request.get_json()
    current_user.firstname=data.get('firstname')
    current_user.lastname = data.get('lastname')
    db.session.commit()
    return 'OK',200




@app.route('/updateAboutUser',methods=['POST'])
@login_required
def updateAboutUser():
    data = request.get_json()
    current_user.about_user=data.get('about_user')
    current_user.address = data.get('address')
    db.session.commit()
    return 'OK',200




def dateModifier(time):
    months = [
            'Jan','Feb','March','April','May','June',
            'July','Aug','Sep', 'Oct','Nov','Dec'
            ]
    dateArray = time.split('/')
    mod_date = months[int(dateArray[0]) - 1] + ' ' + dateArray[1]
    return mod_date

@app.route('/profile')
@login_required
def profile():
    joined_date = dateModifier(current_user.account_date.strftime('%m/%Y'))
    return render_template('users/profile.html', title='Profile', joined_date=joined_date)




def save_pic(pic):
    random_hex = secrets.token_hex(16)
    _, ext = os.path.splitext(pic.filename)
    mod_pic = random_hex + ext
    path = os.path.join(app.config['UPLOAD_PATH'], 'static', 'user-images', mod_pic)
    pic.save(path)
    return mod_pic

def delete_pic(file):
    if file != 'default.png' or file != 'header.jpg':
        path = os.path.join(app.config['UPLOAD_PATH'], 'static', 'user-images', file)
        try:
            os.remove(path)
        except:
            pass

@app.route('/avatar', methods=['GET', 'POST'])
@login_required
def avatar():
    form=UploadAvatarForm()
    if form.validate_on_submit():
        if form.profile_pic.data:
            delete_pic(current_user.profile_pic)
            current_user.profile_pic = save_pic(form.profile_pic.data)
        if form.header_pic.data:
            delete_pic(current_user.header_pic)
            current_user.header_pic = save_pic(form.header_pic.data)
        db.session.commit()
        flash('Your account details has been updated', 'info')
        return redirect(url_for('avatar'))
    return render_template('users/avatar.html', title='Avatar', form=form)

