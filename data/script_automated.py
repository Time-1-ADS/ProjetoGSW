import json
import sys
import psycopg2

from psycopg2 import connect, Error

with open('jira.json') as json_data:
    record_list = json.load(json_data)

if type(record_list) == list:
    first_record = record_list[0]

    columns = list(first_record.keys())
    print("\ncolumn names:", columns)

columns = [list(x.keys()) for x in record_list][0]

table_name = "projetos"
sql_string = 'INSERT INTO {}'.format(table_name)
sql_string += "("+', '.join(columns)+")\nVALUES "


for i, record_dict in enumerate(record_list):

    values = []
    for col_name, val in record_dict.items():

        if type(val) == str:
            val = val.replace("'", "''")
            val = "'" + val + "'"

        values += [str(val)]
    sql_string += "(" + ','.join(values) + "),\n"

sql_string = sql_string[:-2] + ";"


try:

    conn = connect(
        dbname="dashboard",
        user="admin3",
        host="127.0.0.1",
        password="admin321",

        connect_timeout=3
    )

    cur = conn.cursor()
    print("\ncreated cursor object: ", cur)


except(Exception, Error) as err:
    print("\npsycopg2 connect error:", err)
    conn = None
    cur = None


if cur != None:

    try:
        cur.execute(sql_string)
        conn.commit()

        print('\nfinished INSERT INTO execution')

    except (Exception, Error) as error:
        print("\nexecute_sql() error:", error)
        conn.rollback()

    cur.close()
    conn.close()
