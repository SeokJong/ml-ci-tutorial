import unittest

import main


class MainTest(unittest.TestCase):
    def test_hello(self):
        ret = main.hello("Test")
        self.assertEqual(ret,"hello world: Test")

if __name__ == "__main__":
    unittest.main()