import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """ Create a connection to postgre DB
        Set the session property with auto commit= true to commit  after every execution
        return variables for connection and cursor
        
        
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    conn.close()    
        
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """for all the queries in the List drop_table_queries execute each statement and commit"""
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """for all the queries in the List create_table_queries execute each statement and commit"""
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()


if __name__ == "__main__":
    main()