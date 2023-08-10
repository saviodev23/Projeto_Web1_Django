# Projeto_Web1_Django

# Sistema de Locação de Carros

Este é um sistema de locação de carros desenvolvido utilizando o framework Django. O sistema permite que clientes cadastrem-se e façam reservas de carros disponíveis na locadora. Além disso, o sistema conta com uma interface administrativa que permite que funcionários da locadora gerenciem as reservas, carros e clientes.


### Diagrama de Classe do Professor:
![DiagramaClasse](https://github.com/saviodev23/Projeto_Web1_Django/assets/132952225/d8bd07b4-a0bc-4713-a4e5-cd1eaf640056)

### Diagrama de Entidade e Relacionamento Gerado do Projeto:
![DER_locacao](https://github.com/saviodev23/Projeto_Web1_Django/assets/132952225/c4f46668-60fd-4b7a-967d-b599619f3d07)



## Funcionalidades Principais

- Cadastro de clientes: Os clientes podem se cadastrar no sistema, fornecendo informações como usuário, primeiro nome, segundo nome, email e senha.

- Listagem de carros: O sistema exibe vários cards de carros disponíveis para locação e de carros já alugados no momento, com informações sobre a marca, modelo, valor da locação por dia e uma breve descrição do carro.

- Reserva de carros: Os clientes podem fazer reservas de carros disponíveis, informando a data e hora de locação e devolução. O vendedor e Gerente da empresa também pode fazer a locação para o cliente.

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

### O sistema contém 3 grupos de usuarios, que são: Cliente, Vendedor e Gerente. 

#### GERENTE:
O grupo "Gerente" possui as permissões mais abrangentes dentro do sistema. Eles têm total controle sobre todas as funcionalidades e recursos. Isso inclui a capacidade de adicionar, editar e excluir registros de veículos, reservas e clientes.


#### VENDEDOR:
O grupo "Vendedor" possui um conjunto mais amplo de permissões em comparação aos clientes. Além das funcionalidades de visualização, eles têm a capacidade de executar ações mais avançadas, como adicionar novos registros de veículos, efetuar reservas em nome dos clientes, atualizar informações de reservas existentes e fornecer assistência em todo o processo de locação. No entanto, os vendedores não têm a autorização para excluir registros do banco de dados, garantindo assim a integridade dos dados.

#### CLIENTE:
Os usuários do grupo "Cliente" têm um acesso restrito e são principalmente focados em visualização. Eles podem navegar pelo sistema, visualizar informações sobre carros disponíveis, efetuar reservas e verificar o status das suas próprias reservas. No entanto, eles não têm permissão para realizar ações que afetam a estrutura do sistema, como adicionar, editar ou excluir registros no banco de dados.

O usuário cliente é criado no momento de registro no sistema, automáticamente é vinculado ao grupo de Cliente.

