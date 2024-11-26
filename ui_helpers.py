import sqlite3

# Function to initialize the database
def initialize_db(db_file):
    conn = sqlite3.connect(db_file)
    conn.close()
