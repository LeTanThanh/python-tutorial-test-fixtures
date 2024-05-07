from unittest import TestCase

def setUpModule():
  print("Running setUpModule")

class TestMyModule(TestCase):
  @classmethod
  def setUpClass(cls):
    print("Running setUpClass")

  def setUp(self):
    print('\nRunning setUp')

  def test_case_1(self):
    print("Running test_case_1")
    self.assertEqual(5 + 5, 10)

  def test_case_2(self):
    print("Running test_case_2")
    self.assertEqual(1 + 1, 2)

  def tearDown(self):
    print("Running tearDown")

  @classmethod
  def tearDownClass(cls):
    print("Running tearDownClass")

def tearDownModule():
  print("Running tearDownModule")
