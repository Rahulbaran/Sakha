from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length



class CreatePostForm(FlaskForm):
    content=TextAreaField('Content', validators=[Length(max = 5000, message = 'Upto 5000 characters are allowed')])
    postImage = FileField('Upload Image', validators=[FileAllowed(['jpg','png','gif','svg', 'jpeg'],
                                                        message = 'Image with extension jpg/png/gif/svg is only allowed')])
    submit = SubmitField('Create Post')



class EditPostForm(FlaskForm):
    content=TextAreaField('Content', validators=[Length(max = 5000, message = 'Upto 5000 characters are allowed')])
    postImage = FileField('Upload Image', validators=[FileAllowed(['jpg','png','gif','svg', 'jpeg'],
                                                        message = 'Image with extension jpg/png/gif/svg is only allowed')])
    submit = SubmitField('Update Post')



class CommentForm(FlaskForm):
    body = TextAreaField(validators=[Length(max = 1000, message = 'Upto 1000 characters are allowed')])
    submit = SubmitField('Comment')



