import unittest
from app import app

class UserAPITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_users(self):
        response = self.client.get('/api/users', headers={"Role": "user"})
        self.assertEqual(response.status_code, 200)
    
    def test_create_user(self):
        new_user = {"name": "Jane Doe", "email": "jane@example.com"}
        response = self.client.post('/api/users', json=new_user, headers={"Role": "admin"})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
