import unittest
import string

from configui.utils.coherse_name import coherse_name, valid_characters

class TestCoherseName(unittest.TestCase):
    bad_name = '\n~This -is- &a# bad "name".\t'
    def test_contents(self):
        for character in coherse_name(self.bad_name):
            self.assertTrue(character in valid_characters)

if __name__ == '__main__':
    unittest.main()
