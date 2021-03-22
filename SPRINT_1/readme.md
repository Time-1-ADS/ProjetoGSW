## :bookmark: Primeira Entrega - SPRINT 1

<br>

Nessa sprint focamos em entregar o código e algumas funcionalidades importantes de acordo com o seguinte card:
<h1 align="center"> <img src = "/Imagens Geral/card_1.png" width="710" height="420" /></h1>

<br>

## :mag_right: Visão do Projeto

A empresa parceira desenvolve projetos de sistemas para Comércio Exterior, Compliance
fiscal, soluções SAP, Microsoft Dynamics AX/365, software Contábil/Fiscal e, também atua com Fábrica de Software.
Com mais de 500 colaboradores e mais de 900 projetos por ano, evidencia-se a necessidade de condensar as informações de status desses projetos, para auxiliar na tomada de decisões.
Dessa maneira a GSW, em parceria com a FATECSJC, propõem através da Aprendizagem por Projetos Integrados o desenvolvimento da aplicação.

**O problema é:** Apresentar, de forma resumida, o status do andamento dos
projetos, em um único Dashboard;

**Que afeta** as análises para tomada de decisão em curto e médio prazo;

**O impacto disto é** permitir à Direção, ter uma noção global dos processos
referentes aos negócios em TI, podendo visualizar também, de
forma dinâmica e objetiva, dados referentes a projetos
específicos;

**A solução seria** O desenvolvimento de aplicação que permita a unificação e tratamento dos dados para análise.

<br>

## :black_nib: Escopo da Solução
Abaixo elencamos as necessidades identificadas em consulta aos stakeholders, classificando-as: 

| Necessidades | Categorias |
| :--- | :---: |
| 1. Estruturação de Base de Dados local, baseada em SQL, com a finalidade de unificar e normalizar os dados oriundos dos sistemas de gerenciamento de projetos | Essencial |
| 2. Desenvolvimento de aplicação WEB que permita integrar o BD com o Dashboard. | Essencial |
| 3. Geração de relatórios analíticos. | Importante |
| 4. Aperfeiçoar a interface, de modo a proporcionar uma boa representação visual dos dados. | Importante |
| 5. Saída com análises adicionais, proporcionando múltiplos relatórios e gráficos. | Desejável |

:pushpin: **Principais deliverables**

Após a conclusão do projeto os seguintes “deliverables” deverão ser produzidos e entregues:

> Plano de Teste

> Manual de Operação

<br>

## :rocket: Branches das Entregas

| Sprints/Entregas do Projeto | Deliverables | Data de Início | Data de Término |
| :---: | :---: | :---: | :---: |
| `SPRINT 1` | Layout Figma e Dashboard Inicial | 08/03/2021 | 28/03/2021 |
| `SPRINT 2` | Status dos Projetos e Incrementos no Dashboard | 29/03/2021 | 18/04/2021 |
| `SPRINT 3` | Aprimoramento e mais requisitos do cliente | 26/04/2021 | 16/05/2021 |
| `SPRINT 4` | Sprint Bônus com entregas de valor e correção de erros | 17/05/2021 | 05/06/2021 |

<br>

## :chart_with_downwards_trend: Burndown da Equipe

<img src = "/Imagens Geral/burndowngrafic.png" width="600" height="450"/></h1>

<br>

## :elephant: Dados PostgreSQL
**O cliente forneceu os dados dos projetos (.json), sendo eles:**
> :space_invader: [Jira e Trello](https://github.com/Time-1-ADS/ProjetoGSW/tree/main/data)

<br>

## :computer: Requisitos para instalação do projeto


**Instalação:**

- Create your venv

```
$ python -m venv <venvname>
```

- Activate your venv
```
$ ./venvname/Scripts/activate
```

- Clone the repository
```
$ git clone https://github.com/Time-1-ADS/ProjetoGSW
```

- Install requirements
```
$ pip install requirements.txt
```

- Create the role on PostgreSQL
```
CREATE ROLE admin3 WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD 'admin321';
```

- Restore database
```
// Restore the database using the pgadmin
```

**Go to folder where have the file manage.py**

- Create migrate on database
```
$ python manage.py migrate
```

- Run server
```
$ python manage.py runserver
```