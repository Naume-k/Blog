from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
datetime.utcnow()


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    blogs= db.relationship('Blog',backref = 'user',lazy = "dynamic")
    
  
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}' 

class Blog(db.Model):
    
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref='blog',lazy='dynamic')
    

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls,id):
        blogs = Blog.query.filter_by(blog_id=id).all()
        return blogs

    @classmethod
    def clear_blog(cls):
        Blog.blog.clear()

    def delete(self, id):
        comments = Comment.query.filter_by(id = id).all()
        for comment in comments:
            db.session.delete(comment)
            db.session.commit()
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Blog {self.description}'

class Comment(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"

class Quotes:
    '''
    Quotes class to define quote objects
    '''

    def __init__(self,quote,author):

        self.quote = quote
        self.author = author
        



