import json
from collections import Counter
from psycopg2 import connect
from psycopg2.extras import Json

# Abrindo o arquivo.
jira_json_file = open(file='jira.json')

# Lendo o arquivo como Json.
jira_data = json.load(jira_json_file)

# Fechando o arquivo, visto que ele não é mais necessário.
jira_json_file.close()

# CONVERTENDO

jira_list = []

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
    jira_list.append(jira_details)

# Criando arquivo do jira
with open('jira_formatted.json', 'w') as f:
    json.dump(jira_list, f, ensure_ascii=False)


# Verificando quantidades

status_tags = ['DONE', 'FOR_TEST', 'IN_PROGRESS', 'RELEASE_TO_PROD', 'PROD_DEPLOYING', 'QA_DEPLOYING', 'QA_TESTING']
ks = 0
ttl = len(status_tags)
i = 0
jira_status_quant = []
tot = len(jira_list)
while ks < ttl:
  k = 0
  q = 0
  while k < tot:

    palavras_procuradas = {status_tags[ks]}
    texto = [jira_list[k]["status"]]


    dicionario = {}
    for palavra in texto:
        if palavra in palavras_procuradas:
            count = 1
            if palavra in dicionario:
              count = int(dicionario[palavra].split(' ')[-1]) + 1;
            dicionario[palavra] = palavra + " " + str(count)
          

    for palavra in palavras_procuradas:
      if palavra not in texto:
        dicionario[palavra] = palavra + " " + str(0)

    for chave in dicionario:
        if(dicionario[palavra] == palavra + " " + str(1)):
          q = q + 1
    k = k + 1
  ks = ks + 1

  jira_q = {chave: None}
  jira_q [chave] = q
  jira_status_quant.append(jira_q)


# Criando arquivo com quantidades
with open('jira_q.json', 'w') as f:
    json.dump(jira_status_quant, f, ensure_ascii=False)
