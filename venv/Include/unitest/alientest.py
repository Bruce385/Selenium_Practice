import unittest

class AlienTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("TestCase  start running ")

    def test_1_run(self):
        print("hello world_1")

    def test_2_run(self):
        print("hello world_2")

    def test_3_run(self):
        print("hello world_3")

if __name__=='__main__':
    unittest.main()