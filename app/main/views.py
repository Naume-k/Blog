from . import main
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import *
from .forms import BlogForm,UpdateProfile, CommentForm,UpdateBlogForm
from .. import db,photos
from .. requests import get_quotes
from flask_login import login_required, current_user

import markdown2 
@main.route('/blog/<int:id>')
def single_blog(id):
    Blog=Blog.query.get(id)
    if blog is None:
        abort(404)
    format_blog = markdown2.markdown(blog.blog,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('blog.html',blog = blog,format_blog=format_blog)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    get_blogs = Blog.query.filter_by(user_id = current_user.id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, blog_category = get_blogs)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    quotes = get_quotes()
    blogs = Blog.query.all()
    return render_template('index.html',blogs=blogs,quotes = quotes)    


@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    blogs = Blog.query.all()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        author_id = current_user
        print(current_user._get_current_object().id)
        new_blog = Blog(user_id =current_user._get_current_object().id, title = title,description=description)#,category=category)
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('main.index' ))
    return render_template('blog.html',form=form,blogs=blogs)



@main.route('/comment/new/<int:blog_id>', methods = ['GET','POST'])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    blog=Blog.query.get(blog_id)
    if form.validate_on_submit():
        description = form.description.data
        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, blog_id = blog_id)#user_id=user_id,
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', blog_id= blog_id))

    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    return render_template('comments.html', form = form, comment = all_comments, blog = blog )


@main.route('/index/<int:id>/delete', methods = ['GET','POST'])
@login_required
def delete(id):
    current_post = Blog.query.filter_by(id = id).first()

    if current_post.user != current_user:
        abort(404)
    db.session.delete(current_post)
    db.session.commit()
    return redirect(url_for('.index'))

@main.route('/index/<int:id>/delete_comment', methods = ['GET','POST'])
@login_required
def delete_comment(id):

    current_post = Comment.query.filter_by(id = id).first()

    if current_post.user != current_user:
        abort(404)

    db.session.delete(current_post)
    db.session.commit()
    return redirect(url_for('.index'))
    return render_template('comments.html',current_post = current_post)


@main.route('/update/<int:id>',methods= ['GET','POST'])
@login_required
def update_blog(id):

    blogs = Blog.query.filter_by(id = id).first()
    if blogs.user!=current_user:
        abort(404)

    form = UpdateBlogForm()

    if form.validate_on_submit():

        blogs.title = form.title.data
        blogs.description = form.description.data

        db.session.add(blogs)
        db.session.commit()

        return redirect(url_for('main.index'))
    elif request.method=='GET':
            form.description.data=blogs.description
            form.title.data=blogs.title
    return render_template('updateblog.html',form = form)
    


