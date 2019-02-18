from django.test import TestCase
import unittest
# Create your tests here.

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()




# class evenTestCase(unittest.TestCase):
#
#     def __init__(self,number):
#         self.number = number
#
#     def Enum(self):
#         if self.number%2==0:
#             return True
#         else:
#             return False
#
#     def is_Enum(self):
#         self.assertTrue()
#
#
#
# if __name__ == '__main__':
#     unittest.main()