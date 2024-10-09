import unittest
from app import app

class CustomerSegmentationTestCase(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.app = app.test_client()
        self.app.testing = True

    # Test valid input case
    def test_valid_prediction(self):
        response = self.app.post('/', data={
            'total_spend': '1000',  # Assume this is the total spend for a year
            'frequency': '10'       # Assume this is the purchase frequency in a year
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Predicted Segment', response.data)

    # Test edge case with zero values
    def test_zero_input(self):
        response = self.app.post('/', data={
            'total_spend': '0',
            'frequency': '0'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Predicted Segment', response.data)

    # Test for negative values
def test_negative_input(self):
    response = self.app.post('/', data={'total_spend': -10, 'frequency': -5})
    self.assertIn(b'Negative values are not allowed.', response.data)


    # Test for invalid input (non-numeric)
    def test_invalid_input(self):
        response = self.app.post('/', data={
            'total_spend': 'abc',
            'frequency': 'xyz'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input!', response.data)

if __name__ == '__main__':
    unittest.main()
