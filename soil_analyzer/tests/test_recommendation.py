import unittest
from soil_analyzer.recommendation import recommend_crops, recommend_amendments

class TestRecommendation(unittest.TestCase):
    def test_recommend_crops(self):
        sample = {'pH': 5.2, 'moisture': 0, 'organic_matter': 0, 'sand': 0, 'silt': 0, 'clay': 0}
        crops = recommend_crops(sample)
        self.assertIn('potato', crops)
        self.assertIn('blueberry', crops)

    def test_recommend_amendments(self):
        sample = {'pH': 5.0, 'organic_matter': 2, 'moisture': 0, 'sand': 0, 'silt': 0, 'clay': 0}
        recs = recommend_amendments(sample)
        self.assertIn('apply lime or wood ash to raise pH', recs)
        self.assertIn('add compost or manure to increase organic matter', recs)

if __name__ == '__main__':
    unittest.main()
