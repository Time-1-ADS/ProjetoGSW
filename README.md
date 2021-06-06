<div align="center">
<h5 align="center"> Seja Bem-Vindo a Branch de Aplicação </h5>

<br>

<p align="center">
      <img src="https://github.com/Time-1-ADS/ProjetoGSW/blob/sprints/Imagens%20Geral/imginicial.png" width="200" height="150">
<p align="center">

<p>Este projeto está divido por branches, acesse o repositório com as informações do projeto: </p>

<br />

[**Saiba mais**](https://github.com/Time-1-ADS/ProjetoGSW) |
[Dashboard](http://dashboardgsw.herokuapp.com)

<br />
</div>

<br>

## :rocket: GSW Dashboard está no ar

🔗 **[Clique aqui](http://dashboardgsw.herokuapp.com)** para acessar o Dashboard Online no Heroku.

<br>

  _Nota 1: A aplicação web está em produção no Heroku, conforme indicado pelo cliente. Sendo protegida com acesso de Login e Senha._
 
  _Nota 2: O presente projeto tem apenas fins didáticos, portanto não cumprirá a Lei n° 13.853, de 08/07/2019 da Lei Geral de Proteção de Dados Pessoais (LGPD) em sua totalidade._

<br>

## :ringed_planet: Links das API's 

Com base nos dados disponibilizados pelo cliente, organizamos os arquivos (json), **[Clique aqui](https://apigsw.herokuapp.com/)** para mais detalhes.

<br>

## :cloud: Banco de Dados na Nuvem

O Banco de Dados deste projeto está integrado no sistema Cloud AWS da Amazon.

<br>

## :computer: Como instalar o GSW Dashboard?


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

<br>

## :mortar_board: Conheça nossa Equipe 

|Nome|Função|LinkedIn|GitHub|Avatar|
| -------- |-------- |-------- |-------- |-------- |
|**Bryan Ribeiro**|Scrum Master|[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://linkedin.com/in/bryanrribeiro/)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/BryanRibeiro)|<img src = "https://media-exp1.licdn.com/dms/image/C4E03AQEqjHK3s2KQ9g/profile-displayphoto-shrink_800_800/0/1614391630089?e=1626912000&v=beta&t=7Wk-nGEpy8Ug3IaCBaw4LwKh4nCq6Z3LD7BtgxuiOcM" height="50"/>|
|**Danilo Pires**|Product Owner|[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/Danilo2010)|<img src = "https://raw.githubusercontent.com/Time-1-ADS/ProjetoGSW/sprints/Imagens%20Geral/fotodanilo.jpeg" height="50"/>|
|**Lucas César**|Desenvolvedor 1|[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucas-cesar-2020k/)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/LucasACES)|<img src = "https://avatars.githubusercontent.com/u/66032756?s=400&u=031b12f3adce22b79bad8791b1a30a7ead840cea&v=4" height="50"/>|
|**Marcus Rocha**|Desenvolvedor 2|[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/marcus-vin%C3%ADcius-augusto-rocha-568bb8192/)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/mvarocha)|<img src = "https://avatars.githubusercontent.com/u/71012953?s=460&u=28b8bad2bb28aefe147fe3ba39de5af03ed62e43&v=4" height="50"/>|
|**Jeferson Henrique**|Desenvolvedor 3|[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/jeferson-silva-249884149/)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/JefersonHenrique)|<img src = "https://avatars.githubusercontent.com/u/71130553?s=460&u=3f2eb7fb8915bfb53bf3393d2af1cec1139dc770&v=4" height="50"/>|
|**Raphael Prado**|Desenvolvedor 4|[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/raphael-lisboa-7b3597187/)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/raphaelprado)|<img src = "https://avatars.githubusercontent.com/u/71613664?s=460&u=e49bfb545a1e97319b3dd2b42ecc1f56498fd1c2&v=4" height="50"/>|
|**Elias Ferreira**|Desenvolvedor 5|[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/elias-ferreira-525ba41b6/)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/elias31072002)|<img src = "https://avatars.githubusercontent.com/u/71013006?s=400&u=cdaf1fd724434cc5928dec38453bce0b3ee5f98a&v=4" height="50"/>|

<br>

 <h1 align="center"> <img src = "https://raw.githubusercontent.com/Grupo-1-2020-PI-FATEC-ADS/SOS-EDUCA/master/Imagens%20Geral/logo%20fatec.png" height="90" /></h1>
