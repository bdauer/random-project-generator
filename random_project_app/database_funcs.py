import psycopg2

# create a db
# get the project table working
# query the project table
# create a basic page for generating a random project.


# Connect to an existing database
>>> conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
>>> cur = conn.cursor()

def create_table(table_name, *columns):
    pass


def add_row(table_name, *columns):
    pass

def update_table(table_name, *columns)
