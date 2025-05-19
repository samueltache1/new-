import importlib
import unittest

import soil_analyzer.config as config
import soil_analyzer.analysis as analysis

class TestAnalysis(unittest.TestCase):
    def test_classify_ph_default(self):
        self.assertEqual(analysis.classify_ph(5.0), 'acidic')
        self.assertEqual(analysis.classify_ph(6.5), 'optimal')
        self.assertEqual(analysis.classify_ph(7.5), 'alkaline')

    def test_classify_ph_custom_config(self):
        original = config.IDEAL_PH_RANGE
        config.IDEAL_PH_RANGE = (5.5, 6.5)
        try:
            importlib.reload(analysis)
            self.assertEqual(analysis.classify_ph(6.7), 'alkaline')
        finally:
            config.IDEAL_PH_RANGE = original
            importlib.reload(analysis)

if __name__ == '__main__':
    unittest.main()
