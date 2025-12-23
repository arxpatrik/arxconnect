ARXConnect

ARXConnect é um sistema interno web desenvolvido em Python/Django para uso administrativo/organização de tarefas e usuários dentro da empresa ARX. 
GitHub

🧠 Visão Geral

Este projeto oferece uma interface administrativa para gerenciamento de usuários, pendências, dashboards e configurações internas — tudo estruturado como um aplicativo web modular com Django. 
GitHub

🚀 Funcionalidades

✔️ Autenticação e gestão de usuários

✔️ Painéis personalizados (dashboards)

✔️ Visualização e controle de pendências

✔️ Estrutura modular por app Django

✔️ Configurações internas organizadas por módulos

✔️ Front-end com HTML, CSS e JavaScript

✔️ Banco de dados SQLite para desenvolvimento rápido

🧩 Estrutura de Pastas

O projeto possui a seguinte estrutura básica (conforme visualizado no repositório):

/
├── arxconnect/        # Código principal do projeto Django
├── configs/           # Configurações adicionais
├── dashboards/        # Módulo de dashboards
├── home/              # Página inicial
├── pendencias/        # Gerenciamento de pendências
├── usuarios/          # Gestão de usuários
├── db.sqlite3         # Banco de dados SQLite (desenvolvimento)
├── manage.py          # Script de comandos Django
├── requirements.txt   # Dependências Python
└── .gitignore
``` :contentReference[oaicite:3]{index=3}

🛠️ Tecnologias Utilizadas

| Tecnologia | Versão / Descrição |
|------------|---------------------|
| Python     | Backend principal |
| Django     | Framework web MVC |
| SQLite     | Banco de dados (dev) |
| HTML/CSS/JS| Front-end básico |
| Outras libs| Dependências listadas em *requirements.txt* |

*(Instale as versões específicas conforme o seu requirements.)* :contentReference[oaicite:4]{index=4}


## 🚀 Começando

### Pré-requisitos

Antes de iniciar, verifique se você tem:

- Python 3.x instalado  
- pip / venv configurado  

### Instalação

1. Clone o repositório: 
   git clone https://github.com/arxpatrik/arxconnect.git
   cd arxconnect

Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows


Instale as dependências:

pip install -r requirements.txt


Aplique as migrations:

python manage.py migrate


Execute o servidor:

python manage.py runserver


Acesse no navegador:

http://localhost:8000



