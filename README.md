# :computer: GesEdu: API em Django Rest Framework para auxílio a aplicações de Gestão de Alunos

<h2 align="left">Considerações Iniciais</h2>

=> VERSÃO ATUAL UTILIZA DATABASE MYSQL LOCAL, Porem, já esteve hospedado em nuvem, as informações abaixo se referem a 1º versão da API.

=> BANCO DE DADOS: MySQL hospedado em nuvem pelo RailWay

=> [https://railway.app/](%E2%80%B8https://railway.app/)

=> Foi escolhido e utilizado o RailWay para hospedagem do banco, a opção foi feita PRINCIPALMENTE por ele ser um database EM NUVEM o qual selecionei como MySQL, creio ser uma opção criativa em vista do pouco tempo e também de concorrentes ap cargp.

<p align="center">
  <img src="https://github.com/marciodelfinooliveira/Back-Fabrica/assets/141946311/9261905c-c91f-4197-b7c9-645bf91dcb8b" />
</p>

<p align="center">
  <img src="https://github.com/marciodelfinooliveira/Back-Fabrica/assets/141946311/1a3a7aab-cee2-4d35-ac3a-33c3661b3d11" />
</p>

<p align="center">
  <img src="https://github.com/marciodelfinooliveira/Back-Fabrica/assets/141946311/b45c2769-dc7f-486a-9d37-fc5eb4df332c" />
</p>

<h2 align="left">Configurando o Ambiente</h2>

Para executar a API Primeiro se certifique de executar os seguintes códigos abaixo:

Fazer clone do Repositório

>> git clone https://github.com/marciodelfinooliveira/Back-Fabrica.git
>>

Com o repositório aberto, execute a Venv

>> python -m venv venv
>>

Ative a Venv

>> venv\Scripts\activate
>>

Instale as dependências do projeto

>> pip install -r requirements.txt
>>

Aplique as Migrações do Banco de Dados

>> python manage.py migrate
>>

Finalmente, execute o servidor

>> python manage.py runserver
>>

<h2 align="left">Requiremets.txt</h2>

- asgiref==3.7.2
- Django==4.2.4
- django-cors-headers==4.2.0
- djangorestframework==3.14.0
- mysqlclient==2.2.0
- node==1.2.1
- odict==1.9.0
- plumber==1.7
- python-dotenv==1.0.0
- pytz==2023.3
- sqlparse==0.4.4
- tzdata==2023.3
- zope.component==6.0
- zope.deferredimport==5.0
- zope.deprecation==5.0
- zope.event==5.0
- zope.hookable==5.4
- zope.interface==6.0
- zope.lifecycleevent==5.0
- zope.proxy==5.0.0

<h2 align="left">Realização do CRUD</h2>

<h4 align="left"> Models </h4>

- Foram definidos os modelos das apps nos seus respectivos arquivos de models
- Foram criadas as classes que herdam as models.Model, estas classes representam as entidades presentes no aplicativo
- Foram definidos os campos das models usando classes como models.CharField, models.IntegerField, etc.
- Foram adicionados as relações entre as entidades, de forma mais específica, as apps do projeto são Alunos, Professores e Cursos.
- Aluno recebe uma Foreign.Key de Curso, pois um aluno pode assistir aulas de um curso de sua escolha
- Curso recebe uma Foreign.Key de Professores, pois um curso só pode acontecer se existir um professor vinculado a este.

<h4 align="left"> Serializers </h4>

- Foram criados os Serializers de todas as entidades
- As classes que herdam de serializers.ModelSerializer para serializar e desserializar seus modelos foram criadas.
- Foi criado a classe Meta em todas as serializers de todas as entidades

<h4 align="left"> Viewsets </h4>

- Foram criados as Viewsets de todas as entidades
- As classes que herdam de viewsets.ModelSerializer usadas para definir conjuntos de visualizações (viewsets) que fornecem uma maneira conveniente de criar um CRUD

<h4 align="left"> URLs (Rotas) </h4>

- As urls.py das entidades foram criados e configurados
- Foi usado router para simplificar a configuração de urls
- Foram associados as urls as views via métodos path

<h4 align="left"> Migrações </h4>

- foram feitas as migrações via makemigrations e migrate

<h4 align="left"> Execução do Servidor </h4>

- O servidor de desenvolvimento foi iniciado usando o comando runserver.
- Foram executadas as solicitações http (GET, POST, PUT, DELETE) para criar, ler, atualizar e excluir registros.
