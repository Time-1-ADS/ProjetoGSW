import json

from psycopg2 import connect
from psycopg2.extras import Json
from unidecode import unidecode


def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

# Abrindo o arquivo.

trello_json_file = open(file='trello.json', encoding='utf-8')
jira_json_file = open(file='jira.json', encoding='utf-8')

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
    trello_details["usuario_first_name"] = unidecode(item["user"]["userName"])
    trello_details["usuario_last_name"] = unidecode(item["user"]["userLastName"])
    trello_details["usuario_email"] = item["user"]["userEmail"]
    trello_details["amounthours"] = item["hours"]
    if item["hours"] == None:
        trello_details["amounthours"] = 0
    trello_details["startedat"] = item["startedAt"]
    trello_details["finished"] = item["isFinished"]
    trello_details["project"] = unidecode(item["project"])
    trello_details["carddescription"] = unidecode(item["cardDescription"])
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
    jira_details["usuario_first_name"] = unidecode(item["user"]["first_name"])
    jira_details["usuario_last_name"] = unidecode(item["user"]["last_name"])
    jira_details["usuario_email"] = item["user"]["email"]
    jira_details["amounthours"] = item["amountHours"]
    if item["amountHours"] == None:
        jira_details["amounthours"] = 0
    jira_details["startedat"] = item["startedAt"]
    jira_details["finished"] = item["finished"]
    jira_details["project"] = unidecode(item["project"])
    jira_details["carddescription"] = unidecode(item["cardDescription"])
    jira_details["gitmetadata_branch"] = item["gitMetadata"]["branch"]
    jira_details["gitmetadata_hash"] = item["gitMetadata"]["hash"]
    data_list.append(jira_details)

# Separando dados para as tabelas FUNCIONARIO e PROJETOS
# FUNCIONARIOS:
func_list = []
for item in data_list:
    sp_details = {"usuario_id": None, "usuario_first_name": None,
                  "usuario_last_name": None, "usuario_email": None, "usuario_avatar": None, }
    sp_details["usuario_id"] = item["usuario_id"]
    sp_details["usuario_first_name"] = item["usuario_first_name"]
    sp_details["usuario_last_name"] = item["usuario_last_name"]
    sp_details["usuario_email"] = item["usuario_email"]
    sp_details["usuario_avatar"] = item["usuario_avatar"]
    func_list.append(sp_details)

with open('funcionarios.json', 'w') as f:
    json.dump(func_list, f, ensure_ascii=False)

# PROJETOS:
proj_list = []
for item in data_list:
    spr_details = {"id": None, "status": None, "amounthours": None, "startedat": None, "project": None,
                   "carddescription": None, "gitmetadata_branch": None, "gitmetadata_hash": None, "finished": None, }
    spr_details["id"] = item["id"]
    spr_details["status"] = item["status"]
    spr_details["amounthours"] = item["amounthours"]
    spr_details["startedat"] = item["startedat"]
    spr_details["project"] = item["project"]
    spr_details["carddescription"] = item["carddescription"]
    spr_details["startedat"] = item["startedat"]
    spr_details["gitmetadata_branch"] = item["gitmetadata_branch"]
    spr_details["gitmetadata_hash"] = item["gitmetadata_hash"]
    spr_details["finished"] = item["finished"]
    proj_list.append(spr_details)


# Criando arquivo

with open('dadosFormatados.json', 'w') as f:
    json.dump(data_list, f, ensure_ascii=False)
    print("Arquivo formatado!\n")


# contando status

status_tags = ['DONE', 'FOR_TEST', 'IN_PROGRESS',
               'RELEASE_TO_PROD', 'PROD_DEPLOYING', 'QA_DEPLOYING', 'QA_TESTING']
ks = 0
ttl = len(status_tags)
i = 0
data_status_quant = []
data_status_list = [["Status", "Quantidade"]]
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

ppa = q

# Criando arquivo com quantidades
with open('./statusCount/status_count.json', 'w') as f:
    json.dump(data_status_list, f, ensure_ascii=False)
    print("Total de status criado!\n")

# pegando os projetos


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


# status por projeto

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
    #print(f"projeto {fcont}")
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

                        #print(f"task {scont}")
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
                with open(f'./statusCountProject/status_count_{ppjx}.json', 'w') as f:
                    json.dump(data_status_list, f, ensure_ascii=False)
                data_status_quant = []
                data_status_list = [["Status", "Quantidade"]]
                dicippj = {}

    fcont += 1

print("Status por projeto criado!\n")


# allTask_finished

terminado = [True, False]
ks = 0
ttl = len(terminado)
i = 0
data_status_quant = []
data_status_list = [["Status", "Quantidade"]]
tot = len(data_list)
while ks < ttl:
    k = 0
    q = 0
    while k < tot:

        palavras_procuradas = {terminado[ks]}
        texto = [data_list[k]["finished"]]

        dicionario = {}
        for palavra in texto:
            if palavra in palavras_procuradas:
                count = 1
                if palavra in dicionario:
                    count = int(dicionario[palavra].split(' ')[-1]) + 1
                dicionario[palavra] = str(palavra) + " " + str(count)

        for palavra in palavras_procuradas:
            if palavra not in texto:
                dicionario[palavra] = str(palavra) + " " + str(0)

        for chave in dicionario:
            if(dicionario[palavra] == str(palavra) + " " + str(1)):
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
with open('./taskFinished/tasksfinishedAll.json', 'w') as f:
    json.dump(data_status_list, f, ensure_ascii=False)

print("Quantidade de tasks criado!\n")


# task_finished by project

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
    #print(f"projeto {fcont}")
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
                        palavras_procuradas = {terminado[stt]}
                        texto = [data_list[scont]["finished"]]
                        for palavra in texto:
                            if palavra in palavras_procuradas:
                                count = 1
                                if palavra in dicippj:
                                    count = int(
                                        dicippj[palavra].split(' ')[-1]) + 1
                                dicippj[palavra] = str(
                                    palavra) + " " + str(count)

                        for palavra in palavras_procuradas:
                            if palavra not in texto:
                                dicippj[palavra] = str(palavra) + " " + str(0)

                        for chav in dicippj:
                            if(dicippj[palavra] == str(palavra) + " " + str(1)):

                                if chav == palavra:
                                    q = q + 1
                                    data_c = {chav: q}

                        #print(f"task {scont}")
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
            if stt == ttl:
                gravar = 0
                with open(f'./taskFinishedProject/taskfinished{ppjx}.json', 'w') as f:
                    json.dump(data_status_list, f, ensure_ascii=False)
                data_status_quant = []
                data_status_list = [["Status", "Quantidade"]]
                dicippj = {}

    fcont += 1

print("Quantidade de tasks por projeto criado!\n")

# nome e sobrenome
nome1 = []
nome2 = []
nome = []
foto = []
j = 0
tt = len(data_list)
ii = 0

while j < tt:
    first = [data_list[j]["usuario_first_name"]]
    last = [data_list[j]["usuario_last_name"]]
    avatar = [data_list[j]["usuario_avatar"]]
    for primeiro in first:
        rem = unidecode(primeiro)
        if rem not in nome1:
            nome1.append(rem)
            for ultimo in last:
                rem = unidecode(ultimo)
                nome2.append(rem)
            for link in avatar:
                foto.append(link)
    j = j + 1

nome.append(nome1)
nome.append(nome2)
nome.append(foto)
with open(f'./nome-sobrenome/nomeAll.json', 'w') as f:
    json.dump(nome, f, ensure_ascii=False)

print("Nome e sobrenome criado\n")

# nome e sobrenome projeto
for projeto in ppj:
    juncao = []
    for name in nome1:
        i = 0
        soma = 0
        while i < len(data_list):
            first = data_list[i]["usuario_first_name"]
            rem = unidecode(first)
            horas = data_list[i]["amounthours"]
            projetox = data_list[i]["project"]
            if rem == name and projetox == projeto:
                horasAt = horas
                soma = round(soma + horasAt, 2)

                i += 1
            else:
                i += 1
        juncao.append(soma)

    if len(nome) == 4:
        nome[3] = juncao
    else:
        nome.append(juncao)
    with open(f'./nome-sobrenome-projeto/{projeto}.json', 'w') as f:
        json.dump(nome, f, ensure_ascii=False)


print("Nome e sobrenome por projeto criado\n")

# Criando lista com apenas projeto e horas.
list_data = []
for item in data_list:
    dd_details = {"project": None, "amounthours": None, }
    dd_details["project"] = item["project"]
    dd_details["amounthours"] = item["amounthours"]
    list_data.append(dd_details)

# Armazenando a quantidade de projetos do dadosFormatados na variavel l.
l = len(data_list)
ll = l - 1
# Armazenando
pcl = len(ppj)

# Separando os projetos e tirando os iguais.
z = 0
hp = []
pj = []
v = 1999
n = 1
while(z < pcl):
    while(list_data[v]['project'] in pj):
        v = v - 1

    while(n < l):
        if list_data[v]['project'] == list_data[n]['project']:
            n = n + 1

        else:
            n = n + 1

    pj.append(list_data[v]['project'])
    v = v - 1
    n = 1
    z = z + 1

# Somando as horas por projeto.
z = 0
m = 0
v = 0
n = 0
while(z < pcl):
    k = 0
    if pj[z] in hp:
        z = z + 1

    while(n < l):
        if pj[z] == list_data[n]['project']:
            k = k + list_data[n]['amounthours']
            m = m + list_data[n]['amounthours']
            n = n + 1
        else:
            n = n + 1

    # Armazenando a soma de horas do projeto


    k = truncate(k, 2)
    # k = "%.2f" % k
    x = f"{k}"
    y = float(x)
    hp.extend([pj[z], y])
    # Criação do arquivo json por projeto
    with open(f'./horas-por-projeto/horas_projeto_{pj[z]}.json', 'w') as f:
        json.dump(hp, f, ensure_ascii=False)
    n = 1
    z = z + 1
    hp = []

print("Horas total por projeto criado\n")

# Horas total
z = 0
m = 0
v = 0
n = 0
hp = []
while(z < pcl):
    k = 0
    if pj[z] in hp:
        z = z + 1

    while(n < l):
        if pj[z] == list_data[n]['project']:
            m = m + list_data[n]['amounthours']
            n = n + 1
        else:
            n = n + 1

    n = 1
    z = z + 1

# Armazenando a soma de horas do projeto
x = f"{m:.0f}"
y = int(x)
hp.append(y)


with open(f'./sum-horas/horastotal.json', 'w') as f:
    json.dump(hp, f, ensure_ascii=False)

print("Soma total das horas criado\n")

#Tirando a média de horas por projeto.
hp = []
z = 0
m = 0
v = 0
n = 0
clr = 0
while(z < pcl):
        k = 0
        if pj[z] in hp:
            z = z + 1

        while(n < l):
            if pj[z] == list_data[n]['project']:
                k = k + list_data[n]['amounthours']
                n = n + 1
                #clr é a variável que vai armazenar a quantidade de um projeto especifico
                clr = clr + 1
            else:
                n = n + 1

        #Armazenando a soma de horas do projeto e dividindo para tirar a média
        x = f"{k}"
        y = float(x) / clr
        x = f"{y:.2f}"
        y = float(x)
        hp.extend([pj[z], y])
        #Criação do arquivo json de média de horas por projeto
        with open(f'./media-horas-por-projeto/media_horas_projeto_{pj[z]}.json', 'w') as f:
            json.dump(hp, f, ensure_ascii=False)
        n = 1
        z = z + 1
        hp = []
        clr = 0

print("Media de horas por projeto criado\n")

# Média de horas total
z = 0
m = 0
v = 0
n = 0
hp = []
while(z < pcl):
    k = 0
    if pj[z] in hp:
        z = z + 1

    while(n < l):
        if pj[z] == list_data[n]['project']:
            m = m + list_data[n]['amounthours']
            n = n + 1
        else:
            n = n + 1

    n = 1
    z = z + 1

# Armazenando a soma de horas do projeto
x = f"{m}"
# Dividindo o valor total pela quantidade de projetos (a quantidade de projetos está armazenado na variável l)
y = float(x) / l
x = f"{y:.2f}"
y = x
hp.append(y)


with open(f'./media-sum-horas/media_horas_total.json', 'w') as f:
    json.dump(hp, f, ensure_ascii=False)

print("Media do total das horas criado\n")

# criando uma lista com apenas os dados que vão ser utilizados para os códigos relacionados a colaboradores.
colab_list = []
for item in data_list:
    cb_details = {"usuario_first_name": None, "usuario_last_name": None, "usuario_email": None,
                  "usuario_avatar": None, "usuario_id": None, "amounthours": None, "finished": None, }
    cb_details["usuario_first_name"] = item["usuario_first_name"]
    cb_details["usuario_last_name"] = item["usuario_last_name"]
    cb_details["usuario_email"] = item["usuario_email"]
    cb_details["usuario_avatar"] = item["usuario_avatar"]
    cb_details["usuario_id"] = item["usuario_id"]
    cb_details["amounthours"] = item["amounthours"]
    cb_details["finished"] = item["finished"]
    if item["finished"] == True:
        cb_details["finished"] = 1
    else:
        cb_details["finished"] = 0

    colab_list.append(cb_details)


# criando uma lista para colocar os id's dos usuários
colab = []

j = 0

# tirando id's repitidos utilizando a função remove_repetidos
tt = len(data_list)
ii = 0
while j < tt:
    txto = [data_list[j]["usuario_id"]]
    for projeto in txto:
        colab.append(projeto)
        j = j + 1

colab = remove_repetidos(colab)
# pcll é a variável onde contém a quantidade de colaboradores
pcll = len(colab)


# Dados dos colaboradores + tasks abertas e fechadas
z = 0
m = 0
v = 0
n = 0
h = 0
t = 0
lt = []
while(z < pcll):
    k = 0
    if colab[z] in hp:
        z = z + 1

    while(n < l):
        if colab[z] == colab_list[n]['usuario_id']:
            # armazenando dados em variáveis
            cuf = colab_list[n]['usuario_first_name']
            cul = colab_list[n]['usuario_last_name']
            cue = colab_list[n]['usuario_email']
            cua = colab_list[n]['usuario_avatar']
            # calculando a quantidade de tasks abertas e fechadas
            if(colab_list[n]['finished'] == 1):
                # h = task aberta
                h = h + 1
            else:
                # t = task fechada
                t = t + 1
            n = n + 1

        else:
            n = n + 1

    # Colocando os dados na lista lt.
    fn = str(cul)
    inf = str(cuf)
    lt.extend([
        # colab[z] é a lista onde contém os id's dos usuários
        colab[z],
        cuf,
        cul,
        cue,
        cua,
        h,
        t,
    ])
    # Criação do arquivo json de cada colaborador
    with open(f'./tasks-por-colaborador/{inf}_{fn}.json', 'w') as f:
        json.dump(lt, f, ensure_ascii=False)
    n = 1
    z = z + 1
    h = 0
    t = 0
    # limpando a lista
    lt = []

print("Tasks abertas e fechadas por colaborador criado\n")


# Horas mensal e anual por colaborador
z = 0
v = 0
n = 0
h = 0
t = 0
lt = []
while(z < pcll):
    k = 0
    if colab[z] in hp:
        z = z + 1

    while(n < l):
        if colab[z] == colab_list[n]['usuario_id']:
            # armazenando dados em variáveis
            cuf = colab_list[n]['usuario_first_name']
            cul = colab_list[n]['usuario_last_name']
            cua = colab_list[n]['usuario_avatar']
            # calculando a quantidade de tasks abertas e fechadas
            k = k + colab_list[n]['amounthours']
            n = n + 1

        else:
            n = n + 1

    # Convertendo o valor de k para float
    x = f"{k:.0f}"
    # Y será horás anual.
    y = int(x)
    # Calculando horas mensal.
    m = y / 12
    mm = f"{m:.0f}"
    mmm = int(mm)

    # Colocando os dados na lista lt.
    fn = str(cul)
    inf = str(cuf)
    lt.extend([
        # colab[z] é a lista onde contém os id's dos usuários
        colab[z],
        cuf,
        cul,
        cua,
        mmm,
        y,
    ])
    # Criação do arquivo json de cada colaborador
    with open(f'./horas-por-colaborador/{inf}_{fn}.json', 'w') as f:
        json.dump(lt, f, ensure_ascii=False)
    n = 1
    z = z + 1
    h = 0
    t = 0
    # limpando a lista
    lt = []

print("Horas por ano e horas por mês por colaborador criado\n")

with open('projetos.json', 'w') as f:
    json.dump(proj_list, f, ensure_ascii=False)

    # Inserindo projetos no database

with open('projetos.json') as json_data:
    record_list = json.load(json_data)

if type(record_list) == list:
    first_record = record_list[0]

    columns = list(first_record.keys())
    # print("\ncolumn names:", columns)

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
        dbname="myDatabase",
        user="administrador",
        host="dashboard-gsw-fatec.cyrmoymsjutf.sa-east-1.rds.amazonaws.com",
        password="teste321",

        connect_timeout=3
    )

    cur = conn.cursor()
    # print("\ncreated cursor object: ", cur)


except(Exception, Error) as err:
    print(f"psycopg2 connect error: {err}\n")
    conn = None
    cur = None


if cur != None:

    try:
        cur.execute(sql_string)
        conn.commit()

        print('INSERT finalizado dentro de projetos\n')

    except (Exception, Error) as error:
        print(f"execute_sql() error: {error}\n")
        conn.rollback()

    cur.close()
    conn.close()

# Inserindo funcionarios no database
with open('funcionarios.json') as json_data:
    record_list = json.load(json_data)

if type(record_list) == list:
    first_record = record_list[0]

    columns = list(first_record.keys())
    # print("\ncolumn names:", columns)

columns = [list(x.keys()) for x in record_list][0]

table_name = "funcionarios"
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
        dbname="myDatabase",
        user="administrador",
        host="dashboard-gsw-fatec.cyrmoymsjutf.sa-east-1.rds.amazonaws.com",
        password="teste321",

        connect_timeout=3
    )

    cur = conn.cursor()
    # print("\ncreated cursor object: ", cur)


except(Exception, Error) as err:
    print(f"psycopg2 connect error: {err}\n")
    conn = None
    cur = None


if cur != None:

    try:
        cur.execute(sql_string)
        conn.commit()

        print('INSERT finalizado dentro de funcionarios\n')

    except (Exception, Error) as error:
        print(f"execute_sql() error: {error}\n")
        conn.rollback()

    cur.close()
    conn.close()
