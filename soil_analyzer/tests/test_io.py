import os
import tempfile
import unittest
from unittest.mock import patch

from soil_analyzer.io import read_csv


class TestReadCsv(unittest.TestCase):
    def make_csv(self, content: str) -> str:
        tmp = tempfile.NamedTemporaryFile('w+', delete=False)
        tmp.write(content)
        tmp.flush()
        tmp.close()
        return tmp.name

    def test_valid_texture(self):
        path = self.make_csv("pH,moisture,organic_matter,sand,silt,clay\n6,20,4,40,40,20\n")
        with patch('click.echo') as echo:
            rows = read_csv(path)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['sand'], 40.0)
        echo.assert_not_called()
        os.remove(path)

    def test_invalid_texture_warns(self):
        path = self.make_csv("pH,moisture,organic_matter,sand,silt,clay\n6,20,4,30,30,30\n")
        with patch('click.echo') as echo:
            rows = read_csv(path)
        self.assertEqual(len(rows), 1)
        echo.assert_called_once()
        os.remove(path)


if __name__ == '__main__':
    unittest.main()
