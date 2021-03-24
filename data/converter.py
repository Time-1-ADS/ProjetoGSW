import json

from psycopg2 import connect
from psycopg2.extras import Json

# Abrindo o arquivo.
jira_json_file = open(file='jira.json')
trello_json_file = open(file='trello.json')

# Lendo o arquivo como Json.
jira_data = json.load(jira_json_file)
trello_data = json.load(trello_json_file)

# Fechando o arquivo, visto que ele não é mais necessário.
jira_json_file.close()
trello_json_file.close()

# Transformando a lista em string.
dados = str(jira_data)
data = str(trello_data)

# Deixando letras minúsculas.
letter = dados.lower()
lttr = data.lower()

# Trocando 'user' por 'person'.
x = letter.replace("user", "person")

y = lttr.replace("user", "person")
z = y.replace("_id","id")
y = z.replace("personname","first_name")
z = y.replace("personlastname","last_name")
y = z.replace("personemail","email")
z = y.replace("hours","amounthours")
y = z.replace("isfinished","finished")

# Criando arquivo formatado.
with open('jira_formatted.json', 'w') as f:
  json.dump(x, f)
with open('trello_formatted.json', 'w') as f:
  json.dump(y, f)
