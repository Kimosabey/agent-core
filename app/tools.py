import sqlite3
from langchain_core.tools import tool
from .config import Config

# Setup a simple database for the agent to query
def setup_dummy_database():
    conn = sqlite3.connect(Config.SQLITE_DB_PATH)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        signup_date TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount REAL,
        order_date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    
    # Seed data if empty
    cursor.execute("SELECT count(*) FROM users")
    if cursor.fetchone()[0] == 0:
        users = [
            (1, "Alice Smith", "alice@example.com", "2023-01-15"),
            (2, "Bob Jones", "bob@example.com", "2023-02-20"),
            (3, "Charlie Brown", "charlie@example.com", "2023-03-10")
        ]
        orders = [
            (101, 1, 99.99, "2023-01-16"),
            (102, 1, 49.50, "2023-02-01"),
            (103, 2, 150.00, "2023-02-21")
        ]
        cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
        cursor.executemany("INSERT INTO orders VALUES (?,?,?,?)", orders)
        conn.commit()
        print("Database seeded.")
    
    conn.close()

# Ensure DB is ready
setup_dummy_database()

@tool
def list_tables() -> str:
    """List all tables in the database."""
    conn = sqlite3.connect(Config.SQLITE_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return str([t[0] for t in tables])

@tool
def describe_table(table_name: str) -> str:
    """Get the schema of a specific table. 
    Args:
        table_name: The name of the table to describe.
    """
    conn = sqlite3.connect(Config.SQLITE_DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        # Format: (cid, name, type, notnull, dflt_value, pk)
        schema = "\n".join([f"{col[1]} ({col[2]})" for col in columns])
        return f"Schema for {table_name}:\n{schema}"
    except Exception as e:
        return f"Error describing table: {e}"
    finally:
        conn.close()

@tool
def execute_sql_query(query: str) -> str:
    """Execute a SQL query against the database.
    Args:
        query: The SQL query to execute.
    """
    # Basic safety check (very naive for POC)
    if not query.strip().lower().startswith("select"):
        return "Only SELECT queries are allowed for safety."
        
    conn = sqlite3.connect(Config.SQLITE_DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return str(results)
    except Exception as e:
        return f"SQL Error: {e}"
    finally:
        conn.close()
