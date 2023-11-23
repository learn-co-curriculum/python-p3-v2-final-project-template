import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def initialize_db():
    """ Initialize the database with required tables """
    database = "timeclock.db"  # Name of the SQLite database file

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        username text NOT NULL,
        password text NOT NULL
    ); """

    sql_create_time_logs_table = """
    CREATE TABLE IF NOT EXISTS time_logs (
        id integer PRIMARY KEY,
        user_id integer NOT NULL,
        clock_in_time text,
        clock_out_time text,
        FOREIGN KEY (user_id) REFERENCES users (id)
    ); """

    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_time_logs_table)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    initialize_db()
