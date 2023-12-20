import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config.config import dbhost, dbname, dbpassword, dbport, dbuser

def connection_to_db():
    try:
        # Connect to current DB
        connection = psycopg2.connect(database = dbname,
                                    user = dbuser,
                                    password = dbpassword,
                                    host = dbhost,
                                    port = dbport)
        # Run autocommit DB
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Create cursor of DB for create query
        cursor = connection.cursor()

        print("Check connect to DB")
        cursor.execute("SELECT version()")
        print(f"Query result: {cursor.fetchone()}")
        
        return cursor
        
    except (Exception, Error) as error:
        
        print(f"PostgreSQL error: {error}")
        return error
    
# Create table (nouns) DB
def create_noun_user():
    
    cursor = connection_to_db()
    
    try:
        cursor.execute("""
                    CREATE TABLE users (
                        id serial primary key,
                        firstname varchar(50) NOT NULL,
                        lastname varchar(128) NOT NULL,
                        age integer,
                        email varchar(256)
                    )
                    """)
        
        print(f"Table USERS created successfully")
    
    except (Exception, Error) as error:
        
        print(f"Create error: {error}")
        return error

def create_noun_post():
    
    cursor = connection_to_db()
    
    try:
        cursor.execute("""
                    CREATE TABLE posts (
                        id serial primary key,
                        author varchar(256) NOT NULL,
                        description text,
                        rating integer DEFAULT 0,
                        added date DEFAULT now(),
                        updated date DEFAULT now()
                    )
                    """)
        
        
        print(f"Table POSTS created successfully")
    
    except (Exception, Error) as error:
        
        print(f"Create error: {error}")
        return error
    # finally:
    #     if connection:
    #         cursor.close()
    #         connection.close()
    #         print("Соединение с PostgreSQL закрыто")
    
def create_tables():
    
    create_noun_user()
    create_noun_post()