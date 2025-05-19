import os
import tempfile
import unittest
from soil_analyzer.io import read_csv


class TestIO(unittest.TestCase):
    def test_read_csv(self):
        csv_content = "pH,moisture,organic_matter,sand,silt,clay\n5.2,30,4,60,30,10\n"
        with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
            tmp.write(csv_content)
            tmp_path = tmp.name
        try:
            samples = read_csv(tmp_path)
            self.assertEqual(len(samples), 1)
            sample = samples[0]
            self.assertEqual(sample['pH'], 5.2)
            self.assertEqual(sample['moisture'], 30.0)
            self.assertEqual(sample['organic_matter'], 4.0)
            self.assertEqual(sample['sand'], 60.0)
            self.assertEqual(sample['silt'], 30.0)
            self.assertEqual(sample['clay'], 10.0)
        finally:
            os.remove(tmp_path)


if __name__ == '__main__':
    unittest.main()
