import unittest
import json
from unittest.mock import patch, MagicMock
from app import app
from user.models import User

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    @patch('user.models.User')
    def test_create_user(self, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = None
        mock_user_instance = MagicMock(
            username= 'test_user', 
            password='password123', 
            email='test@example.com',
            is_active=True
        )
        mock_user.return_value = mock_user_instance

        data = {
            'username': 'test_user', 
            'password': 'password123', 
            'email': 'test@example.com',
            'is_active': True
        }
        response = self.client.post('/api/v1/users/', json=data)
        self.assertEqual(response.status_code, 201)
        # self.assertEqual(json.loads(response.data)['message'], 'User created successfully')

    @patch('user.models.User')
    def test_get_all_users(self, mock_user):

        mock_user_instance1 = MagicMock(
            username= 'test_user1', 
            password='password123', 
            email='test_user1@example.com',
            is_active=True
        )

        mock_user_instance2 = MagicMock(
            username= 'test_user2', 
            password='password123', 
            email='test_user2@example.com',
            is_active=True
        )

        mock_user.query.all.return_value = [mock_user_instance1, mock_user_instance2]

        import pdb;pdb.set_trace()
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, ['user1', 'user2'])

    @patch('user.models.User')
    def test_get_user_by_id(self, mock_user):
        mock_user_instance = MagicMock()
        mock_user_instance.username = 'test_user'
        mock_user_instance.email = 'test@example.com'
        mock_user.query.get_or_404.return_value = mock_user_instance

        response = self.client.get('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['username'], 'test_user')
        self.assertEqual(data['email'], 'test@example.com')

    @patch('user.models.User')
    def test_update_user(self, mock_user):
        mock_user_instance = MagicMock()
        mock_user_instance.username = 'test_user'
        mock_user_instance.email = 'test@example.com'
        mock_user.query.get_or_404.return_value = mock_user_instance

        updated_data = {'username': 'updated_user', 'email': 'updated@example.com'}
        response = self.client.put('/api/v1/users/1', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'User updated successfully')

    @patch('user.models.User')
    def test_delete_user(self, mock_user):
        mock_user_instance = MagicMock()
        mock_user_instance.username = 'test_user'
        mock_user_instance.email = 'test@example.com'
        mock_user.query.get_or_404.return_value = mock_user_instance

        response = self.client.delete('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'User deleted successfully')
