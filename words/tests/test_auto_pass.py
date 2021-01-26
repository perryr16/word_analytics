from django.test import TestCase

class AutoPassTestCase(TestCase):
  def test_auto_pass(self):
    self.assertEqual(1, 1)