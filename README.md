# 🔐 Sistema de Login Django

Sistema completo de autenticação desenvolvido em Django com cadastro, login, logout, dashboard e perfil de usuário.

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Rodar o Projeto](#como-rodar-o-projeto)
- [Acessando o Sistema](#acessando-o-sistema)
- [Comandos Úteis](#comandos-úteis)
- [Estrutura de URLs](#estrutura-de-urls)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Sobre o Projeto

Sistema de autenticação completo que permite:
- Cadastro de novos usuários
- Login e logout
- Dashboard protegido (apenas usuários autenticados)
- Página de perfil
- Sistema de mensagens (feedback visual)
- Redirecionamentos automáticos

---

## ✨ Funcionalidades

- ✅ **Cadastro de Usuários**: Formulário com validação de senha
- ✅ **Login**: Autenticação segura com Django Auth
- ✅ **Logout**: Encerramento de sessão
- ✅ **Dashboard**: Área restrita para usuários logados
- ✅ **Perfil**: Visualização de dados do usuário
- ✅ **Proteção de Rotas**: Páginas protegidas por login
- ✅ **Mensagens de Feedback**: Sucesso, erro, avisos
- ✅ **Redirecionamentos**: Automáticos após login/logout

---

## 🛠️ Tecnologias

- **Python** 3.10+
- **Django** 4.2+
- **SQLite3** (banco de dados)
- **HTML5** (templates)
- **Django Template Language**

---

## 📁 Estrutura do Projeto

```
sistema de login 2/
│
├── core/                          # Configurações principais
│   ├── __init__.py
│   ├── settings.py               # Configurações do Django
│   ├── urls.py                   # URLs principais
│   ├── wsgi.py                   # Servidor WSGI
│   └── asgi.py                   # Servidor ASGI
│
├── accounts/                      # App de autenticação
│   ├── __init__.py
│   ├── views.py                  # Lógica das views
│   └── urls.py                   # Rotas do app
│
├── templates/                     # Templates HTML
│   ├── base.html                 # Template base
│   └── accounts/
│       ├── login.html            # Página de login
│       ├── register.html         # Página de cadastro
│       ├── dashboard.html        # Dashboard
│       └── profile.html          # Perfil do usuário
│
├── venv/                          # Ambiente virtual (não versionar)
├── db.sqlite3                     # Banco de dados (criado após migrate)
├── manage.py                      # Gerenciador Django
├── requirements.txt               # Dependências
├── .gitignore                     # Arquivos ignorados pelo Git
└── README.md                      # Este arquivo
```

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.10 ou superior**
  - Verifique: `python --version`
  - Download: https://www.python.org/downloads/

- **pip** (gerenciador de pacotes Python)
  - Verifique: `pip --version`
  - Geralmente vem com Python

- **Git** (opcional, para clonar o projeto)
  - Verifique: `git --version`
  - Download: https://git-scm.com/

---

## 🚀 Instalação

### Passo 1: Clone ou baixe o projeto

```bash
# Se usar Git
git clone <url-do-repositorio>
cd "sistema de login 2"

# Ou baixe o ZIP e extraia
```

### Passo 2: Crie o ambiente virtual

```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

### Passo 3: Ative o ambiente virtual

```bash
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

**✅ Você saberá que está ativo quando ver `(venv)` no início da linha do terminal**

### Passo 4: Instale as dependências

```bash
pip install -r requirements.txt
```

**Isso instalará:**
- Django 4.2+

### Passo 5: Configure o banco de dados

```bash
# Criar as tabelas no banco de dados
python manage.py migrate
```

**Saída esperada:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

### Passo 6: Crie um superusuário (opcional, mas recomendado)

```bash
python manage.py createsuperuser
```

**Você será solicitado a informar:**
- Username (nome de usuário)
- Email (pode deixar em branco)
- Password (senha - não aparece enquanto digita)
- Password confirmation (confirme a senha)

---

## ▶️ Como Rodar o Projeto

### 1. Certifique-se de que o ambiente virtual está ativo

```bash
# Você deve ver (venv) no início da linha
# Se não estiver ativo, rode:
venv\Scripts\activate
```

### 2. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

**Saída esperada:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 19, 2024 - 10:30:00
Django version 4.2.x, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 3. Acesse o projeto no navegador

Abra seu navegador e acesse:
- **http://127.0.0.1:8000**
- ou **http://localhost:8000**

### 4. Para parar o servidor

Pressione `CTRL + C` no terminal

---

## 🌐 Acessando o Sistema

### Página Inicial
- **URL**: http://127.0.0.1:8000/
- **Redireciona para**: Login

### Cadastro
- **URL**: http://127.0.0.1:8000/accounts/register/
- Crie uma nova conta
- Após cadastro, será redirecionado para login

### Login
- **URL**: http://127.0.0.1:8000/accounts/login/
- Use as credenciais criadas
- Após login, será redirecionado para dashboard

### Dashboard (Protegido)
- **URL**: http://127.0.0.1:8000/accounts/dashboard/
- Requer login
- Exibe saudação com nome do usuário

### Perfil (Protegido)
- **URL**: http://127.0.0.1:8000/accounts/profile/
- Requer login
- Exibe informações do usuário

### Painel Admin
- **URL**: http://127.0.0.1:8000/admin/
- Use as credenciais do superusuário
- Gerencie usuários e dados

### Logout
- **URL**: http://127.0.0.1:8000/accounts/logout/
- Encerra a sessão
- Redireciona para login

---

## 🔧 Comandos Úteis

### Gerenciamento do Servidor

```bash
# Rodar servidor
python manage.py runserver

# Rodar em porta diferente
python manage.py runserver 8080

# Rodar em IP específico
python manage.py runserver 0.0.0.0:8000
```

### Banco de Dados

```bash
# Criar migrações (após alterar models)
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Resetar banco de dados (CUIDADO: apaga tudo)
del db.sqlite3
python manage.py migrate
```

### Usuários

```bash
# Criar superusuário
python manage.py createsuperuser

# Alterar senha de usuário
python manage.py changepassword <username>
```

### Outros

```bash
# Abrir shell interativo do Django
python manage.py shell

# Verificar problemas no projeto
python manage.py check

# Ver todas as URLs disponíveis
python manage.py show_urls  # (requer django-extensions)
```

---

## 🗺️ Estrutura de URLs

| URL | Nome | Descrição | Proteção |
|-----|------|-----------|----------|
| `/` | - | Redireciona para login | Não |
| `/accounts/register/` | register | Cadastro de usuário | Não |
| `/accounts/login/` | login | Login | Não |
| `/accounts/logout/` | logout | Logout | Não |
| `/accounts/dashboard/` | dashboard | Dashboard | ✅ Sim |
| `/accounts/profile/` | profile | Perfil | ✅ Sim |
| `/admin/` | admin | Painel admin | ✅ Sim |

---

## 🐛 Troubleshooting

### Erro: "No module named django"

**Problema**: Django não está instalado

**Solução**:
```bash
# Ative o ambiente virtual
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

---

### Erro: "No module named 'core.urls'"

**Problema**: Arquivo urls.py não encontrado ou com nome errado

**Solução**:
- Verifique se existe `core/urls.py` (com "s")
- Verifique se existe `accounts/urls.py` (com "s")

---

### Erro: "Table doesn't exist"

**Problema**: Banco de dados não foi criado

**Solução**:
```bash
python manage.py migrate
```

---

### Erro: "Port is already in use"

**Problema**: Porta 8000 já está em uso

**Solução**:
```bash
# Use outra porta
python manage.py runserver 8080
```

---

### Erro: "CSRF verification failed"

**Problema**: Token CSRF ausente ou inválido

**Solução**:
- Verifique se `{% csrf_token %}` está nos formulários
- Limpe cookies do navegador
- Use navegação anônima para testar

---

### Ambiente virtual não ativa

**Problema**: Erro ao ativar venv

**Solução Windows**:
```bash
# Tente diferentes métodos
venv\Scripts\activate.bat
venv\Scripts\Activate.ps1

# Ou use CMD ao invés de PowerShell
cmd
venv\Scripts\activate
```

---

### Página não carrega CSS/JS

**Problema**: Arquivos estáticos não configurados

**Solução**:
```bash
# Em desenvolvimento, Django serve automaticamente
# Certifique-se de que DEBUG=True em settings.py

# Para produção, rode:
python manage.py collectstatic
```

---

## 📝 Configurações Importantes

### settings.py

```python
# Idioma e Timezone
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Redirecionamentos
LOGIN_REDIRECT_URL = 'accounts:dashboard'
LOGOUT_REDIRECT_URL = 'accounts:login'
LOGIN_URL = 'accounts:login'

# Debug (SEMPRE False em produção)
DEBUG = True

# Hosts permitidos (configure em produção)
ALLOWED_HOSTS = []
```

---

## 🔒 Segurança

### Para Produção

1. **Altere SECRET_KEY**:
```python
# settings.py
SECRET_KEY = 'sua-chave-secreta-aleatoria-aqui'
```

2. **Desative DEBUG**:
```python
DEBUG = False
```

3. **Configure ALLOWED_HOSTS**:
```python
ALLOWED_HOSTS = ['seudominio.com', 'www.seudominio.com']
```

4. **Use HTTPS**:
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

5. **Use banco de dados robusto**:
- PostgreSQL
- MySQL
- MariaDB

---

## 📚 Próximos Passos

### Melhorias Sugeridas

- [ ] Adicionar recuperação de senha
- [ ] Implementar edição de perfil
- [ ] Upload de foto de perfil
- [ ] Verificação de email
- [ ] Login social (Google, Facebook)
- [ ] Adicionar CSS/Bootstrap
- [ ] Criar testes automatizados
- [ ] Implementar API REST
- [ ] Adicionar paginação
- [ ] Sistema de permissões

---

## 📄 Licença

Este projeto é livre para uso educacional.

---

## 👨‍💻 Autor

Desenvolvido como projeto de estudo de Django.

---

## 📞 Suporte

Se encontrar problemas:

1. Verifique a seção [Troubleshooting](#troubleshooting)
2. Consulte a [documentação oficial do Django](https://docs.djangoproject.com/)
3. Verifique se todas as dependências estão instaladas
4. Certifique-se de que o ambiente virtual está ativo

---

## 🎉 Pronto!

Seu sistema de login Django está funcionando! 🚀

Para começar a usar:
1. Ative o ambiente virtual: `venv\Scripts\activate`
2. Rode o servidor: `python manage.py runserver`
3. Acesse: http://127.0.0.1:8000
4. Crie uma conta e faça login!

**Bom desenvolvimento! 💻**
