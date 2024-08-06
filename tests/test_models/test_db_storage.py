import unittest
from models import storage
from models.state import State


class TestDBStorageMethods(unittest.TestCase):

    def test_get(self):
        state = State(name="California")
        state.save()
        self.assertIsNotNone(storage.get(State, state.id))
        self.assertIsNone(storage.get(State, "non_existent_id"))

    def test_count(self):
        initial_count = storage.count()
        new_state = State(name="Nevada")
        new_state.save()
        self.assertEqual(storage.count(), initial_count + 1)
        self.assertEqual(storage.count(State), 1)


if __name__ == "__main__":
    unittest.main()
