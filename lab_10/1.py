import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='6587009dkssnv'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE phonebook1(
        username VARCHAR(20),
        number VARCHAR(12)
    )
    '''
)
config.commit()

current.close()
config.close()
