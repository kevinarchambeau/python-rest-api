import sqlite3


class SQLite:
    def __init__(self, db):
        self.con = sqlite3.connect(db)

    def get_all_messages(self):
        messages = {}

        cursor = self.con.cursor()
        results = cursor.execute("SELECT * FROM message")

        # result is a tuple
        for result in results:
            messages[result[0]] = result[1]

        return messages

    def get_messages(self, message_id):
        cursor = self.con.cursor()
        try:
            result = cursor.execute("SELECT * FROM message WHERE id = :message_id", [message_id])
        except sqlite3.Error as err:
            print(err)
            return None

        return dict(result)

    # If used in a multiprocess env need to catch if the db is locked
    def insert_message(self, message):
        cursor = self.con.cursor()
        try:
            result = cursor.execute("INSERT INTO message (message) VALUES(?)", [message])
            self.con.commit()
        except sqlite3.Error as err:
            print(err)
            return None

        return result.lastrowid

    def update_message(self, message_id, message):
        data = (message, message_id)
        cursor = self.con.cursor()
        try:
            cursor.execute("UPDATE message SET message = ? WHERE id = ?", data)
            self.con.commit()
        except sqlite3.Error as err:
            print(err)
            return None

        return True

    def delete_message(self, message_id):
        cursor = self.con.cursor()
        try:
            cursor.execute("DELETE FROM message WHERE id = ?", [message_id])
            self.con.commit()
        except sqlite3.Error as err:
            print(err)
            return None

        return True

    def close(self):
        self.con.close()
