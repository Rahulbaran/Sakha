import secrets, os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from Sakha import mail




def registration_mail(user):
    msg = Message('Registration Successful', sender=('Team Sakha', current_app.config['MAIL_USERNAME']), recipients=[user.email])
    msg.html = f'''<h1>🎊 Congratulation {user.firstname + ' ' + user.lastname}</h1>
<p>You have created a brand new account in our platform and we are glad to get you as a new user and welcome you on </b>Sakha</b>.</p>
<p>You can login using the <a href="http://127.0.0.1:5000/login" target="_blank" rel="noreferrer noopener">link</a>.</p>'''
    mail.send(msg)
    


def save_avatar(pic):
    random_hex = secrets.token_hex(16)
    _, ext = os.path.splitext(pic.filename)
    mod_pic = random_hex + ext
    path = os.path.join(current_app.config['UPLOAD_PATH'], 'static', 'user-images', mod_pic)

    img_size = (300,300)
    img = Image.open(pic)
    img.thumbnail(img_size)
    img.save(path)
    return mod_pic



def save_header(pic):
    random_hex = secrets.token_hex(16)
    _, ext = os.path.splitext(pic.filename)
    mod_pic = random_hex + ext
    path = os.path.join(current_app.config['UPLOAD_PATH'], 'static', 'user-images', mod_pic)

    img_size = (1500,1500)
    img = Image.open(pic)
    img.thumbnail(img_size)
    img.save(path)
    return mod_pic



def delete_pic(file):
    if file != 'default.png' and file != 'header.jpg':
        path = os.path.join(current_app.config['UPLOAD_PATH'], 'static', 'user-images', file)
        try:
            os.remove(path)
        except:
            pass



def password_reset_email(user):
    token = user.generate_token()
    msg =f'''<h1>Password Reset Request</h1>
<p>A request has been made to reset your account password, visit the following link \
to reset the password:-</p>
{url_for('resetPassword', token=token, _external=True)}
<p>Above link is valid for 5 minutes only.</p>

<p>If you have not made this request then simply ignore the mail & no changes will be made in your account'''
    mail.send_message(subject = 'Mail for resetting password', \
                            sender=('Team Sakha'), html=msg, recipients=[user.email])
