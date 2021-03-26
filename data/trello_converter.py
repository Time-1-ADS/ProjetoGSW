import json

from psycopg2 import connect
from psycopg2.extras import Json

# Abrindo o arquivo.
trello_json_file = open(file='trello.json')

# Lendo o arquivo como Json.
trello_data = json.load(trello_json_file)

# Fechando o arquivo, visto que ele não é mais necessário.
trello_json_file.close()

# CONVERTENDO

trello_list = []

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
    trello_list.append(trello_details)

# Criando arquivo do trello
with open('trello_formatted.json', 'w') as f:
    json.dump(trello_list, f, ensure_ascii=False)
