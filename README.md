# Projeto_Web1_Django

# Sistema de Locação de Carros

Este é um sistema de locação de carros desenvolvido utilizando o framework Django. O sistema permite que clientes cadastrem-se e façam reservas de carros disponíveis na locadora. Além disso, o sistema conta com uma interface administrativa que permite que funcionários da locadora gerenciem as reservas, carros e clientes.

## Funcionalidades Principais

- Cadastro de clientes: Os clientes podem se cadastrar no sistema, fornecendo informações como nome, CPF, endereço, telefone e email.

- Listagem de carros: O sistema exibe uma lista de carros disponíveis para locação, com informações sobre a marca, modelo, valor da locação por dia e uma breve descrição do carro.

- Reserva de carros: Os clientes podem fazer reservas de carros disponíveis, informando a data e hora de locação e devolução.

- Gerenciamento de reservas: Funcionários da locadora têm acesso a uma interface administrativa que permite visualizar todas as reservas feitas pelos clientes. Eles também podem editar o status das reservas, confirmar ou cancelar as locações.

- Notificações: O sistema envia notificações para os clientes quando uma reserva é confirmada ou cancelada, mantendo-os informados sobre o status da locação.

## Requisitos

- Python 3.x
- Django 3.x
- Banco de dados SQLite (pode ser substituído por outro banco de dados compatível com Django)

## Como Executar o Sistema

1. Clone este repositório para o seu computador.
2. Crie um ambiente virtual e ative-o.
3. Instale as dependências do projeto usando o comando `pip install -r requirements.txt`.
4. Execute as migrações do banco de dados usando o comando `python manage.py migrate`.
5. Crie um superusuário para acessar a interface administrativa usando o comando `python manage.py createsuperuser`.
6. Inicie o servidor de desenvolvimento com o comando `python manage.py runserver`.
7. Acesse a interface administrativa em `http://localhost:8000/admin/` e faça login com o superusuário criado anteriormente.
8. Cadastre carros e clientes no sistema através da interface administrativa.
9. Acesse o site em `http://localhost:8000/` e faça reservas de carros disponíveis.
