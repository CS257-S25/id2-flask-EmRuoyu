"""Unit tests for Flask routes."""
import unittest
from app import app

class TestFlaskRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_route(self):
        """Test the home route returns status 200 and expected content."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'UFO Sightings API', response.data)

    def test_year_route(self):
        """Test the /year/<year> route returns HTML content for dummy year."""
        response = self.client.get("/year/1999")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<table', response.data)  # check that HTML table is present

if __name__ == '__main__':
    unittest.main()
