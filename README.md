# :computer: O repositório contém um exemplo de API criada com Django Rest Framework, a qual possui 3 entidades que se relacionam entre sí.

<h2 align="left">Considerações Iniciais</h2>

-> O Banco de Dados utilizado foi MySQL.

-> O projeto contêm alguns artefatos de segurança, alguns dos quais como o encobrimento de keys e a password do Banco de Dados, logo, se faz necessário a criação do arquivo ".env" para sua execução.

-> O projeto foi desenvolvido com o objetivo de estudo e para pleitear uma vaga em estágio, logo, deixo registrado aqui como consulta a quem interessar.

<h2 align="left">Configurando o Ambiente</h2>

Para executar corretamente a API, primeiro se certifique de executar os seguintes passos abaixo:

-> Fazer o clone do Repositório:

>> git clone https://github.com/marciodelfinooliveira/Back-Fabrica.git

-> Com o repositório aberto, instale o Ambiente Virtual:

>> python -m venv venv

-> Ative-o:

>> ./venv/Scripts/activate

-> Instale as dependências do projeto:

>> pip install -r requirements.txt

-> Crie o arquivo .env, nele insira uma  SECRET_KEY para o projeto ( sugiro o site https://miniwebtool.com/br/django-secret-key-generator/ para geração aleatória de chaves django)

-> Ainda no .env, escreva que DEBUG = 1

-> Ainda no .env, escreva que ALLOWED_HOST = ['127.0.0.1', 'localhost',]

-> Aplique as Migrações do Banco de Dados

>> python manage.py makemigrations
>> python manage.py migrate

-> Finalmente, execute o servidor

>> python manage.py runserver


<h2 align="left">Iterações da API</h2>

Na API, temos uma iteração com um tema de gerenciamento de alunos em cursos, partindo de um caminho em comum, temos PROFESSORES, os quais podemos cadastrar inicialmente, CURSOS, onde podemos alocar um professor existente, e ALUNOS, que podem se matricular nos cursos, e claro, visualizar no Banco qual seu curso e qual seu respectivo professor: 

<p align="center">
  <img src="https://github.com/marciodelfinooliveira/Back-Fabrica/assets/141946311/c8c95199-04b4-4fbf-9063-cd4d04c156d2" />
</p>

Para o cadastro de PROFESSORES, além do nome, email (único) e qual a formação do professor, temos uma validação de CPF, o qual é único, obrigatório e só será aceito caso o CPF seja válido, caso contrário, o cadastro não será realizado

<p align="center">
  <img src="https://github.com/marciodelfinooliveira/Back-Fabrica/assets/141946311/869fe4f9-d290-4557-8bb6-f462e3465ac7" />
</p>

Para o cadastro de CURSOS, além do nome, código (único), descrição, carga horária, turno e nível, é necessário que se cadastre um professor, o qual será responsável por lecionar no curso, porém, esta feature não é obrigatória, podendo se criar um curso sem professor alocado inicialmente, podendo ser alocado posteriormente.

<p align="center">
  <img src="https://github.com/marciodelfinooliveira/Back-Fabrica/assets/141946311/143a94f8-7875-4d80-a93e-3ac104088803" />
</p>

Para o cadastro de ALUNOS, é nome, email (único), CPF (igualmente validado), data de nascimento e qual o curso ele será matriculado, de onde também é possível ele já saber qual o professor está designado ao curso.

<p align="center">
  <img src="https://github.com/marciodelfinooliveira/Back-Fabrica/assets/141946311/59a3f85e-8d99-4205-90fb-b9904098bc61" />
</p>

Um detalhe que não deve passar despercebido é que a API está totalmente paginada.

<p align="center">
  <img src="https://github.com/marciodelfinooliveira/Back-Fabrica/assets/141946311/d78cac78-55ee-4630-9f29-599583f3104d" />
</p>