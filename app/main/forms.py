from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField#, RadioField
from wtforms.validators import Required
class BlogForm(FlaskForm):
   title = StringField('Blog title',validators=[Required()])
   description = TextAreaField('Blog Description', validators=[Required()]) 
   # category = RadioField('Label', choices=[ ('Cute','Cute'), ('Funny','Funny'),('Inspirational','Inspirational'),('Love','Love')],validators=[Required()])
   submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us about your self.',validators = [Required()])
   submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('',validators=[Required()])
	submit = SubmitField()

class UpdateBlogForm(FlaskForm):
   title = StringField('Blog title',validators=[Required()])
   description = TextAreaField('Blog Description', validators=[Required()]) 
   submit = SubmitField('Submit')

# class UpvoteForm(FlaskForm):
# 	submit = SubmitField()

# class Downvote(FlaskForm):
# 	submit = SubmitField()

