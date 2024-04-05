import unittest
from db import SQLite

DB_NAME = "test.db"


# These unit checks are somewhat fragile as test.db could be wiped or content changed.
# TODO generate test db before each run
# If this was a production app more coverage than happy path and some negative checks would be appropriate

class TestSQLite(unittest.TestCase):
    def test_get_all_messages(self):
        db = SQLite(DB_NAME)
        messages = db.get_all_messages()
        self.assertLess(4, len(messages))

    def test_get_message(self):
        db = SQLite(DB_NAME)
        message = db.get_messages("1")
        self.assertEqual(1, len(message))

    def test_get_nonexistent_message(self):
        db = SQLite(DB_NAME)
        message = db.get_messages("999999")
        self.assertEqual(0, len(message))

    def test_insert_message(self):
        db = SQLite(DB_NAME)
        message_id = db.insert_message("weeee")
        self.assertLess(1, message_id)

    def test_delete_message(self):
        db = SQLite(DB_NAME)
        message_id = db.insert_message("weeee")
        self.assertIsNotNone(db.delete_message(message_id))

    def test_update_message(self):
        db = SQLite(DB_NAME)
        self.assertTrue(db.update_message("1", "weeee"))


if __name__ == '__main__':
    unittest.main()
