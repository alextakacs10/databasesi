import psycopg2


def import_sql(filename):
    '''Imports an SQL file used to fill database with sample data.
    '''
    with open(filename, "r") as sqlfile:
        commands = sqlfile.read()
    return commands

def main():
    pass

if __name__ == '__main__':
    main()