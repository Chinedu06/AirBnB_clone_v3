ttest for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
import os

class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class"""

    def setUp(self):
        """Set up for tests"""
        self.storage = FileStorage()
        self.state = State(name="California")
        self.state.save()

    def tearDown(self):
        """Tear down for tests"""
        del self.state
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test the all method"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("State.{}".format(self.state.id), all_objs)

    def test_new(self):
        """Test the new method"""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_obj.id), all_objs)

    def test_save(self):
        """Test the save method"""
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        self.state.save()
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("State.{}".format(self.state.id), all_objs)

    def test_delete(self):
        """Test the delete method"""
        self.storage.delete(self.state)
        all_objs = self.storage.all()
        self.assertNotIn("State.{}".format(self.state.id), all_objs)

    def test_get(self):
        """Test the get method"""
        obj = self.storage.get(State, self.state.id)
        self.assertEqual(obj, self.state)

    def test_count(self):
        """Test the count method"""
        count_all = self.storage.count()
        count_state = self.storage.count(State)
        self.assertEqual(count_state, 1)
        self.assertEqual(count_all, 1)


if __name__ == '__main__':
    unittest.main()
