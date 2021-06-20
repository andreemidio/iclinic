"# IClinic Challenge"

[![codecov](https://codecov.io/gh/andreemidio/iclinic/branch/main/graph/badge.svg?token=Y8XSDLGJQ9)](https://codecov.io/gh/andreemidio/iclinic)

Projeto Django Rest Framework, baseado em diversas fontes de pesquisa e cursos que fiz para a melhor arquitetura e
separação das responsabilidades.

A arquitetura que uso, me baseei no livro publicado por Pydanny (Daniel
Feldroy)  [Two Scoops of Django 3.x](https://daniel.feldroy.com/pages/books/)

Para esse projeto decidir usar o Sqlite para banco de dados, mas costumo usar o PostgreSQL. Decisão tomada apenas por
eficiência de tempo

Para a utilização do projeto é necessário ter o [Pipenv](https://realpython.com/pipenv-guide/) instalado na máquina.

Usando o projeto.

1 - Digite no terminal, estando dentro do projeto, digite.

``
pipenv shell
``

2 - Após instalação do projeto e dependências, use no terminal.

``pipenv install``

3 - Rodar os testes

``pipenv run pytest . --cov=.``

4 - Para usar o projeto digite.

``
python manage.py runserver
``

Esse projeto, eu criei dois ambientes, staging e production.

iclinic-challenge-andre-stag :  https://iclinic-challenge-andre-stag.herokuapp.com/docs/  <br><br>
iclinic-challenge-andre-prod :  https://iclinic-challenge-andre-prod.herokuapp.com/docs/

O Projeto contem CI/CD com o Heroku e testes integrados.

![Heroku Servers](https://github.com/andreemidio/iclinic/blob/feature/prescriptions/images/2021-06-19%2016_26_32-Window.png?raw=true)

Ambos os ambientes estão com a mesma configuração.

Os recursos que utilizei são:

Heroku Postgres -> Banco de dados. <br>

New Relic APM -> Para monitoria da aplicação e análise de erros.<br>

Sentry -> Para monitoria das exceções da aplicação. <br>

![Resources](https://github.com/andreemidio/iclinic/blob/feature/prescriptions/images/2021-06-19%2016_33_21-Window.png?raw=true)

Adicionei Proxy reverso para encobrir o servidor e o PgBouncer para gerenciar as conexões com o banco de dados.


A modelagem do banco de dados fiz dessa forma para ganhar tempo, mas  o correto, para cada chave ter uma tabela separada para alocar os dados.