import unittest
from soil_analyzer.analysis import classify_ph

class TestAnalysis(unittest.TestCase):
    def test_classify_ph(self):
        self.assertEqual(classify_ph(5.0), 'acidic')
        self.assertEqual(classify_ph(6.5), 'optimal')
        self.assertEqual(classify_ph(7.5), 'alkaline')

if __name__ == '__main__':
    unittest.main()
