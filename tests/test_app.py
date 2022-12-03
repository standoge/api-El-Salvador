import unittest

from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_departaments(self):
        response = self.app.get('/?department=Sonsonate')
        self.assertEqual(response.status_code, 200)

    def test_zonessv(self):
        response = self.app.get('/?zone=Oriental')
        self.assertEqual(response.status_code, 200)

if __name__ = "__main__":
    unittest.main()
