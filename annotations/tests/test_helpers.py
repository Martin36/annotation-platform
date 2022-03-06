from django.test import SimpleTestCase

from annotations.helpers import find_first_missing_int

class TestHelpers(SimpleTestCase):
  
  def test_find_first_missing_int(self):
    input = [1, 2, 4, 7]
    expected = 3
    output = find_first_missing_int(input)
    self.assertEqual(expected, output, "Returns the first int that is missing")
    
    input = [1, 2, 2, 3, 7]
    expected = 4
    output = find_first_missing_int(input)
    self.assertEqual(expected, output, "Returns correct int even if duplicates")
    
    input = [3, 2, 2, 1, 6, 5]
    expected = 4
    output = find_first_missing_int(input)
    self.assertEqual(expected, output, "Returns correct int if list is unsorted")
    
    input = [1, 2, 3, 4]
    expected = 5
    output = find_first_missing_int(input)
    self.assertEqual(expected, output, "Returns next int in sequence if no is missing")

    input = []
    expected = 1
    output = find_first_missing_int(input)
    self.assertEqual(expected, output, "Returns 1 for empty lists")
