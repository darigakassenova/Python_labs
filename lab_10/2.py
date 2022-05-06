import psycopg2, csv

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='6587009dkssnv'
)
current = config.cursor()
arr = []

with open('/Users/dariga/Desktop/PP2/lab_10/add.csv') as f:
    reader = csv.reader(f, delimiter=',')
    
    for row in reader:
        arr.append(row)

sql = '''
    INSERT INTO phonebook1
    VALUES (%s, %s) RETURNING *;
'''

for row in arr:
    current.execute(sql, row)

# final = current.fetchall()
# print(final)

current.close()
config.commit()
config.close()