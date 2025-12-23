# ArxConnect

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-5-green)
![PostgreSQL](https://img.shields.io/badge/postgresql-15-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 📌 Sobre o Projeto

**ArxConnect** é um **ERP interno da ARX**, desenvolvido em **Django**, com o objetivo de **centralizar e integrar sistemas internos** já existentes dentro da empresa.

O projeto atua como um **hub corporativo**, reunindo módulos administrativos, dashboards e funcionalidades internas em uma única plataforma, facilitando a gestão, manutenção e evolução dos sistemas da ARX.

---

## 🎯 Objetivo

- Centralizar sistemas internos da ARX
- Padronizar autenticação e gestão de usuários
- Fornecer dashboards e visões administrativas
- Servir como base para novos módulos internos

---

## 🧱 Funcionalidades

- 👤 Gestão de usuários e permissões
- 📊 Dashboards administrativos
- 📋 Controle de pendências
- 🧩 Estrutura modular baseada em apps Django
- 🔐 Integração entre sistemas internos
- 🗄️ Banco de dados PostgreSQL

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Django 5**
- **PostgreSQL**
- HTML / CSS / JavaScript
- Bootstrap (frontend)
- Git para versionamento

---

## 🚀 Como Rodar o Projeto

### 📌 Pré-requisitos

Antes de começar, você precisa ter instalado:

- Python 3.11+
- PostgreSQL
- Git
- Virtualenv (recomendado)

---

### 📦 Instalação

# Clone o repositório
git clone https://github.com/arxpatrik/arxconnect.git

# Entre no projeto
cd arxconnect

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
⚙️ Configuração do Banco de Dados
O projeto utiliza PostgreSQL.

Crie um banco e configure as variáveis de ambiente (ou ajuste diretamente no settings.py):


Copiar código
DEBUG=True
SECRET_KEY=sua_secret_key
DB_NAME=arxconnect
DB_USER=postgres
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432
🗄️ Migrações e Inicialização


Copiar código
# Criar as migrações
python manage.py makemigrations

# Aplicar as migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Rodar o servidor
python manage.py runserver
Acesse no navegador:


Copiar código
http://localhost:8000
📂 Estrutura do Projeto


Copiar código
arxconnect/
├── arxconnect/        # Configurações principais do Django
├── configs/           # Configurações e utilitários
├── dashboards/        # App de dashboards
├── home/              # Página inicial
├── pendencias/        # Módulo de pendências
├── usuarios/          # Gestão de usuários
├── manage.py
├── requirements.txt
└── .env

🧪 Testes

Copiar código
python manage.py test

🤝 Contribuição

Este é um projeto interno, mas boas práticas são bem-vindas:

Crie uma branch (feature/nova-funcionalidade)

Faça commits claros e objetivos

Teste antes de subir alterações

Abra um Pull Request

📌 Observações
Projeto voltado para uso interno da ARX

Estrutura preparada para crescimento modular

Novos sistemas internos podem ser integrados como apps Django
