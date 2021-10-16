from flask import Blueprint, render_template, request
from Sakha.models import Post


mainbp = Blueprint('mainbp', __name__)





@mainbp.route('/')
@mainbp.route('/home')
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.postDate.desc()).paginate(per_page=5,page=page)
    return render_template('sites/home.html', title='Home', posts=posts)





@mainbp.route('/about_us')
def about_us():
    return render_template('sites/aboutus.html', title='About Us')





@mainbp.route('/contact_us')
def contact_us():
    return render_template('sites/contact.html', title='Contact Us')