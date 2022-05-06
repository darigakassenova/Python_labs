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
    CREATE TABLE snake_exam(
        name VARCHAR(20),
        score VARCHAR(30)

    )
    '''
)
config.commit()

current.close()
config.close()
