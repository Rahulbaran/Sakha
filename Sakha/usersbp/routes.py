from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
from Sakha import db, bcrypt
from Sakha.models import User, Post
from Sakha.usersbp.utils import delete_pic, save_avatar, registration_mail, password_reset_email, save_header
from Sakha.usersbp.form import RegistrationForm, LoginForm, AboutUpdateForm, UploadAvatarForm,\
                             UniqueDetailsUpdateForm, NameUpdateForm, RequestPasswordResetForm, ResetPasswordForm




usersbp = Blueprint('usersbp', __name__)




@usersbp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('mainbp.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data,
                    email=form.email.data ,gender=form.gender.data, password = hashed_pw)
        db.session.add(user)
        db.session.commit()
        # registration_mail(user)
        flash('You have created a brand new account', 'info')
        return redirect(url_for('usersbp.login'))
    return render_template('users/register.html', title='Register Here', form=form)




@usersbp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('mainbp.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            flash(f'Welcome back {user.firstname}, you are logged in', 'info')
            return redirect(next) if next else redirect(url_for('mainbp.home'))
        else:
            flash('Either username or password is wrong', 'warning')
    return render_template('users/login.html', title='Login Here', form=form)




@usersbp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out', 'info')
    return redirect(url_for('mainbp.home'))




@usersbp.route('/settings', methods=['GET', 'POST'])
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
        return redirect(url_for('usersbp.settings'))
    return render_template('users/settings.html', title='Settings',nameForm=nameForm,\
                             aboutForm=aboutForm, uniqueForm=uniqueForm)




@usersbp.route('/updateName',methods=['POST'])
@login_required
def updateName():
    data = request.get_json()
    current_user.firstname=data.get('firstname')
    current_user.lastname = data.get('lastname')
    db.session.commit()
    return {
        'firstname' : current_user.firstname.capitalize(),
        'lastname' : current_user.lastname.capitalize()
    }




@usersbp.route('/updateAboutUser',methods=['POST'])
@login_required
def updateAboutUser():
    data = request.get_json()
    current_user.about_user=data.get('about_user')
    current_user.address = data.get('address')
    db.session.commit()
    return 'OK',200




@usersbp.route('/profile')
@login_required
def profile():
    page = request.args.get('page',1,type=int)
    posts = Post.query.filter_by(userId=current_user.id).order_by(Post.postDate.desc()).paginate(page=page,per_page=5)
    return render_template('users/profile.html', title='Profile', posts=posts)





@usersbp.route('/user_profile/<int:user_id>')
@login_required
def user_profile(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    if user == current_user: return redirect(url_for('usersbp.profile'))
    page = request.args.get('page',1,type=int)
    posts =Post.query.filter_by(userId=user.id).order_by(Post.postDate.desc()).paginate(page=page,per_page=5)
    return render_template('users/userProfile.html', title=f'{user.firstname} \
                         {user.lastname}', user=user, posts=posts)




@usersbp.route('/follow_action', methods=['POST'])
@login_required
def follow_action():
    idData = request.get_json()
    user = User.query.filter_by(id=idData.get('user_id')).first_or_404()
    if user == current_user:
        return redirect(url_for('mainbp.home'))
    if current_user.is_following(user):
        current_user.unfollow(user)
        db.session.commit()
        return {'follow':'follow', 'followers':user.followers.count()}
    else: 
        current_user.follow(user)
        db.session.commit()
        return {'unfollow':'following', 'followers':user.followers.count()}




@usersbp.route('/followers_list')
@login_required
def followers_list():
    return render_template('users/followerslist.html', title='Followers List')




@usersbp.route('/following_list')
@login_required
def following_list():
    return render_template('users/followinglist.html', title='Following List')




@usersbp.route('/user_followers/<int:user_id>')
@login_required
def user_followers(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('users/userFollowers.html', title=f'{user.firstname} {user.lastname} Followers List', user=user)




@usersbp.route('/user_following/<int:user_id>')
@login_required
def user_following(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('users/userFollowing.html', title=f'{user.firstname} {user.lastname} Following List', user=user)




@usersbp.route('/avatar', methods=['GET', 'POST'])
@login_required
def avatar():
    form=UploadAvatarForm()
    if form.validate_on_submit():
        if form.profile_pic.data:
            delete_pic(current_user.profile_pic)
            current_user.profile_pic = save_avatar(form.profile_pic.data)
        if form.header_pic.data:
            delete_pic(current_user.header_pic)
            current_user.header_pic = save_header(form.header_pic.data)
        db.session.commit()
        flash('Your account details has been updated', 'info')
        return redirect(url_for('usersbp.avatar'))
    return render_template('users/avatar.html', title='Avatar', form=form)




@usersbp.route('/request_password_reset', methods=['GET', 'POST'])
def requestPasswordReset():
    if current_user.is_authenticated:
        flash('You should logout to reset your password', 'info')
        return redirect(url_for('mainbp.home'))
    form = RequestPasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            password_reset_email(user)
            flash('An email has been sent to reset password', 'info')
            return redirect(url_for('mainbp.home'))
        else:
            flash('User is not found', 'warning')
    return render_template('users/requestPasswordReset.html', title='Request Password Reset', form=form)




@usersbp.route('/reset_password/<token>', methods=['GET','POST'])
def resetPassword(token):
    if current_user.is_authenticated:
        flash('You should logout to reset password', 'info')
        return redirect(url_for('mainbp.home'))
    user  = User.verify_token(token)
    if user is None:
        flash('The url is either expired or invalid', 'warning')
        return redirect(url_for('mainbp.home'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user.password = hash_pw
        db.session.commit()
        flash('Your password has be changed now you can login', 'info')
        return redirect(url_for('usersbp.login'))
    return render_template('users/resetPassword.html', title='Reset Password', form=form)
