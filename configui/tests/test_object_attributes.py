import unittest

from configui import load

class ObjectAttributes(unittest.TestCase):
    # -- COMMON SETUP --
    with open('test_object_attributes.yaml') as infile:
        config_object = load(infile)
    # -- TESTS --
    def test_not_none(self):
        self.assertFalse(self.config_object is None)

if __name__ == '__main__':
    unittest.main()

