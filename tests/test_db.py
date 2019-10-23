import unittest
from app import db
from app.models import User,Pitch,Comment

class DbUserPitchComment(unittest.TestCase):
    '''
        Test Class to test the behaviour of the db
      '''

    def setUp(self):
        '''
         Set up method that will run before every Test
        '''
        self.test_user = User(username="test_user", email="test_user@tests.com", password='password' )
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        self.user = User.query.filter_by(username= "joe").first()
        db.session.remove(self.user)
        db.session.commit()

    def test_save_user_to_db(self):
        user = User.query.filter_by(username='joe').first()
        self.assertEqual('joe',user.username)



if __name__ == "__main__":
    unittest.main()
