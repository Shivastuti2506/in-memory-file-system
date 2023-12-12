import unittest
import requests
from unittest.mock import patch
from server import app, FileSystemServer

class TestFileSystemServer(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_mkdir(self):
        response = self.client.post('/mkdir', json={'directory_name': 'test_directory'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Directory '/test_directory' created successfully")

    def test_ls(self):
        response = self.client.get('/ls')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['contents'], [])

    def test_cd(self):
        response = self.client.post('/cd', json={'directory_name': 'test_directory'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Current directory changed to '/test_directory'")

    def test_touch(self):
        response = self.client.post('/touch', json={'file_path': 'test_file.txt'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "File '/test_file.txt' created successfully")

    def test_echo(self):
        response = self.client.post('/echo', json={'file_path': 'test_file.txt', 'content': 'Hello, World!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Content written to '/test_file.txt'")

    def test_cat(self):
        response = self.client.get('/cat', query_string={'file_path': 'test_file.txt'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['content'], "Hello, World!")

    def test_grep(self):
        response = self.client.get('/grep', query_string={'file_path': 'test_file.txt', 'pattern': 'Hello'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['matching_lines'], ["Hello, World!"])

if __name__ == '__main__':
    unittest.main()
