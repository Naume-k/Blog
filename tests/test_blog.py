import unittest
from app.models import User,Blog
from app import db

class BlogTest(unittest.TestCase):
    def setUp(self):
        '''
        Sets up all tests
        '''
        self.user_admin = User(username='wecode',password_hash='nana@1',email='kobnaome@gmail.com')
        self.new_blog = Blog(blog='blog1',category='coding',user_id=self.user_admin)

    def tearDown(self):
        '''
        deletes test data tests after every test
        '''
        User.query.delete()
        Blog.query.delete()

    def test_check_instance_variables(self):
        '''
        test the instances
        '''
        self.assertEquals(self.new_blog.blog,blog1')
        self.assertEquals(self.new_blog.category,'coding')
        self.assertEquals(self.new_blog.user_id,self.user_la)

    def test_save_blog(self):
        '''
        test saving in the db
        '''
        self.new_blog.save_blog()
        self.assertTrue(len(Review.query.all())>0)

    def test_get_blog_by_id(self):
        '''
        tests getting blog by id
        '''
        self.new_blog.save_()
        got_blog = Blog.query.get(1)
        self.assertTrue(len(got_blog)==1)