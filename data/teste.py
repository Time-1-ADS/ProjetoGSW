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

# with open('dadosFormatados.json', 'w') as f:
#     json.dump(data_list, f, ensure_ascii=False)


# contando tasks

status_tags = ['DONE', 'FOR_TEST', 'IN_PROGRESS',
               'RELEASE_TO_PROD', 'PROD_DEPLOYING', 'QA_DEPLOYING', 'QA_TESTING']
ks = 0
ttl = len(status_tags)
i = 0
data_status_quant = []
data_status_list = []
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

    for item in data_c:
        aa = []
        aa.append(item)
        aa.append(q)
        data_status_list.append(aa)

# Criando arquivo com quantidades
# with open('status_count.json', 'w') as f:
#     json.dump(data_status_list, f, ensure_ascii=False)

# ? pegando os projetos


def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)

    return l


ppj = []
j = 0


tt = len(data_list)
ii = 0
while j < tt:
    txto = [data_list[j]["project"]]
    for projeto in txto:
        ppj.append(projeto)
        j = j + 1

ppj = remove_repetidos(ppj)


#! status por projeto

fcontm = len(ppj)
scontm = len(data_list)
data_status_quant = []
data_status_list = [["Status", "Quantidade"]]
fcont = 0
scont = 0
stt = 0
dicippj = {}
q = 0
gravar = 0
item = ''
value = ''


while fcont <= fcontm:
    print(f"projeto {fcont}")
    for projet in ppj:
        stt = 0
        ppjx = projet
        while stt < ttl:
            scont = 0

            if projet in ppjx:
                dicippj[projet] = projet + " "
                verificar = [projet]
                while scont < scontm:
                    confir = [data_list[scont]["project"]]
                    verificardois = confir
                    if verificar == verificardois:
                        palavras_procuradas = {status_tags[stt]}
                        texto = [data_list[scont]["status"]]
                        for palavra in texto:
                            if palavra in palavras_procuradas:
                                count = 1
                                if palavra in dicippj:
                                    count = int(
                                        dicippj[palavra].split(' ')[-1]) + 1
                                dicippj[palavra] = palavra + " " + str(count)

                        for palavra in palavras_procuradas:
                            if palavra not in texto:
                                dicippj[palavra] = palavra + " " + str(0)

                        for chav in dicippj:
                            if(dicippj[palavra] == palavra + " " + str(1)):

                                if chav == palavra:
                                    q = q + 1
                                    data_c = {chav: q}

                        print(f"task {scont}")
                        scont += 1
                    else:
                        scont += 1
            for item in data_c:
                aa = []
                aa.append(item)
                aa.append(q)

            data_status_quant.append(data_c)
            data_status_list.append(aa)
            stt += 1
            q = 0
            gravar += 1
            if stt == 7:
                gravar = 0
                with open(f'status_count_{ppjx}.json', 'w') as f:
                    json.dump(data_status_list, f, ensure_ascii=False)
                data_status_quant = []
                data_status_list = [["Status", "Quantidade"]]
                dicippj = {}

    fcont += 1
