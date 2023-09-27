#!/usr/bin/python3
"""
Unittests for the Square class.
"""
import os
import sys
import unittest
from models.square import Square

# Calculate the project directory path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
models_dir = os.path.join(project_dir, 'models')


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_initialization_success(self):
        """
        Test if the Square class initializes successfully
        with provided values for size and id.
        It asserts that the id attribute is
        correctly assigned to the provided values.
        """
        s1 = Square(5, id=5)  # Provide 'id' as 5
        s2 = Square(10, id=6)  # Provide 'id' as 6
        self.assertEqual(s1.id, 5)
        self.assertEqual(s2.id, 6)

    def test_initialization_without_arguments(self):
        """
        Test if an error is raised when trying to initialize
        a Square object without any arguments.
        It expects a TypeError to be raised.
        """
        self.assertRaises(TypeError, Square)


if __name__ == '__main__':
    unittest.main()
