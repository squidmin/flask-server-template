import unittest
from app import app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_hello_world_route(self):
        # Sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # Asserts the status code of the response
        self.assertEqual(result.status_code, 200)

        # Asserts the response body
        self.assertEqual(result.data, b'<p>Hello, World!</p>')


if __name__ == '__main__':
    unittest.main()
