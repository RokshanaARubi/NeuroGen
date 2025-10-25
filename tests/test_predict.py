import unittest
from logic.predict import run_prediction

class TestPrediction(unittest.TestCase):
    def test_prediction_format(self):
        result = run_prediction("rs429358")
        self.assertIsInstance(result, str)
        self.assertTrue("Risk" in result)

    def test_empty_input(self):
        result = run_prediction("")
        self.assertEqual(result, "Invalid input")

if __name__ == '__main__':
    unittest.main()