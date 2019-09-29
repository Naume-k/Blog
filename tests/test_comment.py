import unittest
from app.models import *
from app import db

class TestQuote(unittest.TestCase):

    def setUp(self):
        self.new_quote = Quote(quote_content = "quote one", pitch_category='Cute')
        self.new_comment = Comment(comment_content = "One comment", quote=self.new_quote)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,"One comment")
        self.assertEquals(self.new_comment.quote,self.new_quote, 'quote one')