import json

from psycopg2 import connect
from psycopg2.extras import Json


# Abrindo o arquivo.

trello_json_file = open(file='trello.json')
jira_json_file = open(file='jira.json')

# Lendo o arquivo como Json.

trello_data = json.load(trello_json_file)
jira_data = json.load(jira_json_file)


# Fechando o arquivo, visto que ele não é mais necessário.

trello_json_file.close()
jira_json_file.close()


# CONVERTENDO

data_list = []

for item in trello_data:
    trello_details = {"id": None, "status": None, "usuario_id": None, "usuario_avatar": None, "usuario_first_name": None, "usuario_last_name": None, "usuario_email": None,
                      "amounthours": None, "startedat": None, "finished": None, "project": None, "carddescription": None, "gitmetadata_branch": None, "gitmetadata_hash": None}
    trello_details["id"] = item["_id"]
    trello_details["status"] = item["status"]
    trello_details["usuario_id"] = item["user"]["_id"]
    trello_details["usuario_avatar"] = item["user"]["avatar"]
    trello_details["usuario_first_name"] = item["user"]["userName"]
    trello_details["usuario_last_name"] = item["user"]["userLastName"]
    trello_details["usuario_email"] = item["user"]["userEmail"]
    trello_details["amounthours"] = item["hours"]
    if item["hours"] == None:
        trello_details["amounthours"] = 0
    trello_details["startedat"] = item["startedAt"]
    trello_details["finished"] = item["isFinished"]
    trello_details["project"] = item["project"]
    trello_details["carddescription"] = item["cardDescription"]
    trello_details["gitmetadata_branch"] = item["gitMetadata"]["branch"]
    trello_details["gitmetadata_hash"] = item["gitMetadata"]["hash"]
    data_list.append(trello_details)


for item in jira_data:
    jira_details = {"id": None, "status": None, "usuario_id": None, "usuario_avatar": None, "usuario_first_name": None, "usuario_last_name": None, "usuario_email": None,
                    "amounthours": None, "startedat": None, "finished": None, "project": None, "carddescription": None, "gitmetadata_branch": None, "gitmetadata_hash": None, }
    jira_details["id"] = item["id"]
    jira_details["status"] = item["status"]
    jira_details["usuario_id"] = item["user"]["id"]
    jira_details["usuario_avatar"] = item["user"]["avatar"]
    jira_details["usuario_first_name"] = item["user"]["first_name"]
    jira_details["usuario_last_name"] = item["user"]["last_name"]
    jira_details["usuario_email"] = item["user"]["email"]
    jira_details["amounthours"] = item["amountHours"]
    if item["amountHours"] == None:
        jira_details["amounthours"] = 0
    jira_details["startedat"] = item["startedAt"]
    jira_details["finished"] = item["finished"]
    jira_details["project"] = item["project"]
    jira_details["carddescription"] = item["cardDescription"]
    jira_details["gitmetadata_branch"] = item["gitMetadata"]["branch"]
    jira_details["gitmetadata_hash"] = item["gitMetadata"]["hash"]
    data_list.append(jira_details)


# Criando arquivo

with open('dadosFormatados.json', 'w') as f:
    json.dump(data_list, f, ensure_ascii=False)


# contando tasks

status_tags = ['DONE', 'FOR_TEST', 'IN_PROGRESS',
               'RELEASE_TO_PROD', 'PROD_DEPLOYING', 'QA_DEPLOYING', 'QA_TESTING']
ks = 0
ttl = len(status_tags)
i = 0
data_status_quant = []
tot = len(data_list)
while ks < ttl:
    k = 0
    q = 0
    while k < tot:

        palavras_procuradas = {status_tags[ks]}
        texto = [data_list[k]["status"]]

        dicionario = {}
        for palavra in texto:
            if palavra in palavras_procuradas:
                count = 1
                if palavra in dicionario:
                    count = int(dicionario[palavra].split(' ')[-1]) + 1
                dicionario[palavra] = palavra + " " + str(count)

        for palavra in palavras_procuradas:
            if palavra not in texto:
                dicionario[palavra] = palavra + " " + str(0)

        for chave in dicionario:
            if(dicionario[palavra] == palavra + " " + str(1)):
                q = q + 1
        k = k + 1
    ks = ks + 1

    data_c = {chave: None}
    data_c[chave] = q
    data_status_quant.append(data_c)


# tasks abertas e fechadas


# Criando arquivo com quantidades

with open('status_count.json', 'w') as f:
    json.dump(data_status_quant, f, ensure_ascii=False)


# Inserindo no database

with open('dadosFormatados.json') as json_data:
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

        print('\nfinished INSERT INTO projetos')

    except (Exception, Error) as error:
        print("\nexecute_sql() error:", error)
        conn.rollback()

    cur.close()
    conn.close()
