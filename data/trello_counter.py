import json
from collections import Counter
from psycopg2 import connect
from psycopg2.extras import Json

trello_json_file = open(file='trello_formatted.json')

trello_data = json.load(trello_json_file)

trello_json_file.close()

# Verificando quantidades

status_tags = ['DONE', 'FOR_TEST', 'IN_PROGRESS', 'RELEASE_TO_PROD', 'PROD_DEPLOYING', 'QA_DEPLOYING', 'QA_TESTING']
ks = 0
ttl = len(status_tags)
i = 0
trello_status_quant = []
tot = len(trello_data)
while ks < ttl:
  k = 0
  q = 0
  while k < tot:

    palavras_procuradas = {status_tags[ks]}
    texto = [trello_data[k]["status"]]


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

  trello_q = {chave: None}
  trello_q [chave] = q
  trello_status_quant.append(trello_q)


# Criando arquivo com quantidades
with open('trello_q.json', 'w') as f:
    json.dump(trello_status_quant, f, ensure_ascii=False)
