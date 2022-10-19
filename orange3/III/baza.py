import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ tworzymy tabelę w bazie
    :param conn: Connection object
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_project(conn, project):
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def update_project(conn, project):
    sql = ''' UPDATE projects
              SET name = ? ,
                  begin_date = ?,
                  end_date = ?
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

def select_all_projects(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# create_connection('sqlite-sakila.db')

database = "baza_nr1.sqlite"

sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

conn = create_connection(database)

if conn is not None:
    # create_table(conn, sql_create_projects_table)
    # create_table(conn, sql_create_tasks_table)
    # project = ("Szkolenie Comarch Java", '2023-10-17', '2023-10-19')
    # project_id = create_project(conn, project)
    # update_project(conn, ('wakacje', '2023-07-17', '2023-08-19', 2))
    select_all_projects(conn)