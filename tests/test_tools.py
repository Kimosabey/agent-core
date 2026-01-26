import unittest
from app.tools import list_tables, describe_table, execute_sql_query

class TestTools(unittest.TestCase):
    def test_list_tables(self):
        result = list_tables.invoke({})
        self.assertIn("users", result)
        self.assertIn("orders", result)

    def test_describe_table(self):
        result = describe_table.invoke({"table_name": "users"})
        self.assertIn("id (INTEGER)", result)
        self.assertIn("name (TEXT)", result)

    def test_execute_query(self):
        result = execute_sql_query.invoke({"query": "SELECT count(*) FROM users"})
        self.assertIn("(3,)", result)  # We seeded 3 users

if __name__ == '__main__':
    unittest.main()
