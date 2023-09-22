#!/usr/bin/python3

import os
import sys
import unittest

from models.base import Base

# Calculate the project directory path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
models_dir = os.path.join(project_dir, 'models')


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # Reset the counter before each test

    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_saving_id(self):
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_to_json_string_valid(self):
        pass


if __name__ == '__main__':
    unittest.main()
