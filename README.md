#Instalando o Django
python -m pip install Django

#Criando o projeto
django-admin startproject cms 


cd cms

#Rodar o servidor
python manage.py runserver

#Criando uma aplicação dentro do projeto
python manage.py startapp polls

#Criar dentro do app um arquivo urls.py para direcionar as rotas
#Adicionar a aplicação no urls.py do projeto

#Em setting.py temos DATABASES com ENGINE sendo o dirver de conexao e NAME o nome da base

#Migrate olha para os INSTALLED_APPS em settings.py e cria as tabelas necessárias para que estes funcionem
python manage.py migrate

#No app, models.py, criar o layout das tabelas necessárias

#Colocando em settings.py polls.apps.PollsConfig e rodando o makemigrations, será criado os models no banco de dados
python manage.py makemigrations polls

#Criar um super usuário, acessar em /admin
python manage.py createsuperuser

#No app, admin, registrar os models que vão aparecer no admin

#Para usar em models o imagePicker
python -m pip install Pillow