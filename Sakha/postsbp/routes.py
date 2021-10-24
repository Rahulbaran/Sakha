from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from Sakha import db
from Sakha.models import Post, Comment
from Sakha.postsbp.form import CreatePostForm, EditPostForm, CommentForm
from Sakha.postsbp.utils import save_post_pic
from Sakha.usersbp.utils import delete_pic




postsbp = Blueprint('postsbp', __name__)




@postsbp.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        if form.postImage.data:
            pic = save_post_pic(form.postImage.data)
            post = Post(content=form.content.data, postImage=pic, author=current_user)
        else:
            post = Post(content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('You have created a new post', 'info')
        return redirect(url_for('mainbp.home'))
    return render_template('users/post.html', title='Create Post',\
                                                    form=form, legend='Create Post Form')




@postsbp.route('/edit_post/post-<int:post_id>', methods=['GET','POST'])
@login_required
def edit_post(post_id):
    form = EditPostForm()
    post = Post.query.filter_by(id=post_id).first_or_404()
    if post.author != current_user:
        abort(403)
    if request.method == "GET":
        form.content.data = post.content
    elif form.validate_on_submit():
        if form.postImage.data:
            delete_pic(post.postImage)
            post.postImage = save_post_pic(form.postImage.data)
            post.content = form.content.data
        else:
            post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated','info')
        return redirect(url_for('mainbp.home'))
    return render_template('users/post.html', title='Edit Post', form=form, legend='Edit Post Form')





@postsbp.route('/delete_post/post-<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if post.postImage :
        delete_pic(post.postImage)
    for like in post.likes:
        db.session.delete(like)
    for comment in post.comments:
        db.session.delete(comment)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'info')
    return redirect(url_for('mainbp.home'))




@postsbp.route('/complete_post/post-<int:post_id>', methods=['GET', 'POST'])
@login_required
def complete_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    form = CommentForm()
    if request.method == "POST":
        json_data = request.get_json()
        comment = Comment(body = json_data.get('comment_text'), post_id=post.id, commenter_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        userComment = Comment.query.filter_by(commenter_id=current_user.id).order_by(Comment.timestamp.desc()).first()
        totalComments = post.comments.count()
        commentData = {
            'comment_id' : userComment.id,
            'comment_body' : userComment.body,
            'commenter_avatar': userComment.commented_user.profile_pic,
            'time' : userComment.timestamp.strftime('%d %b %Y'),
            'commenter_id' : userComment.commenter_id,
            'total_comments' : totalComments,
            'firstname': userComment.commented_user.firstname
        }
        return commentData
    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.timestamp.desc()).all()
    return render_template('users/completePost.html', title='Complete Post', 
                                                      post=post, form=form, comments=comments)




@postsbp.route('/like_action', methods=['POST'])
@login_required
def like_action():
    idData = request.get_json()
    post_id = idData.get('post_id')
    post = Post.query.filter_by(id=post_id).first_or_404()
    if current_user.has_liked(post):
        current_user.unlike_post(post)
    else:
        current_user.like_post(post)
    db.session.commit()
    return {'totalLikes' : post.likes.count()}




@postsbp.route('/delete_comment/<int:comment_id>', methods=["POST"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post = comment.commented_post
    if comment.commented_user == current_user or post.author == current_user:
        db.session.delete(comment)
        db.session.commit()
        return redirect(url_for('postsbp.complete_post',post_id=post.id))

