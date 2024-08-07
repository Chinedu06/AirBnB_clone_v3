#!/usr/bin/python3
"""
Contains the TestFileStorage class
"""

import unittest
from models import storage
from models.state import State


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.clean_storage()

    def clean_storage(self):
        """Clean up the storage"""
        keys_to_delete = list(storage.all().keys())
        for key in keys_to_delete:
            del storage._FileStorage__objects[key]

    def test_get(self):
        """Test that get method returns correct object"""
        obj = storage.get(State, self.state.id)
        self.assertEqual(obj, self.state)

    def test_count(self):
        """Test that count method returns correct number of objects"""
        count = storage.count(State)
        self.assertEqual(count, 1)
        total_count = storage.count()
        self.assertEqual(total_count, 1)

    def tearDown(self):
        """Clean up after each test"""
        self.clean_storage()


if __name__ == "__main__":
    unittest.main()
