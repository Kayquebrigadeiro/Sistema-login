# 🔐 Sistema de Login Django

Sistema completo de autenticação desenvolvido em Django com cadastro, login, logout, dashboard, perfil de usuário, recuperação de senha via email e upload de avatar.

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Como Rodar o Projeto](#como-rodar-o-projeto)
- [Estrutura de URLs](#estrutura-de-urls)
- [Configuração de Email](#configuração-de-email)
- [Diário de Modificações](#diário-de-modificações)
- [Melhorias Sugeridas](#melhorias-sugeridas)
- [Troubleshooting](#troubleshooting)
- [Segurança](#segurança)

---

## 🎯 Sobre o Projeto

Sistema de autenticação completo desenvolvido em Django que oferece:
- Cadastro de usuários com email obrigatório
- Sistema de login e logout seguro
- Dashboard protegido para usuários autenticados
- Perfil de usuário com upload de avatar
- Edição completa de perfil (nome, email, avatar)
- Recuperação de senha via email Gmail
- Alteração de senha para usuários logados
- Interface moderna com estética roxa personalizada

---

## ✨ Funcionalidades

### Autenticação
- ✅ **Cadastro**: Formulário com validação de senha e email obrigatório
- ✅ **Login**: Autenticação segura com Django Auth
- ✅ **Logout**: Encerramento de sessão
- ✅ **Recuperação de Senha**: Token seguro enviado por email (válido por 1 hora)

### Perfil de Usuário
- ✅ **Visualização**: Exibe username, email, nome completo e data de cadastro
- ✅ **Edição**: Atualização de dados pessoais
- ✅ **Avatar**: Upload e exibição de foto de perfil
- ✅ **Alteração de Senha**: Mudança de senha para usuários logados

### Segurança
- ✅ **Proteção de Rotas**: Páginas protegidas por login
- ✅ **Mensagens de Feedback**: Sucesso, erro e avisos
- ✅ **Variáveis de Ambiente**: Credenciais protegidas em arquivo .env
- ✅ **Tokens Seguros**: Sistema de recuperação de senha do Django

---

## 🛠️ Tecnologias

- **Python** 3.10+
- **Django** 4.2+
- **SQLite3** (banco de dados)
- **Pillow** (processamento de imagens)
- **python-dotenv** (variáveis de ambiente)
- **Gmail SMTP** (envio de emails)
- **HTML5 + CSS3** (interface)

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes)
- Git (opcional)

### Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/Kayquebrigadeiro/Sistema-login.git
cd Sistema-login

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o arquivo .env (copie do .env.example)
cp .env.example .env
# Edite o .env com suas credenciais de email

# 5. Execute as migrações
python manage.py migrate

# 6. Crie perfis para usuários existentes (se necessário)
python create_profiles.py

# 7. Rode o servidor
python manage.py runserver
```

### Acesse o sistema
- **URL**: http://127.0.0.1:8000
- Crie uma conta e faça login!

---

## 🗺️ Estrutura de URLs

| URL | Nome | Descrição | Proteção |
|-----|------|-----------|----------|
| `/` | - | Redireciona para login | Não |
| `/accounts/register/` | register | Cadastro de usuário | Não |
| `/accounts/login/` | login | Login | Não |
| `/accounts/logout/` | logout | Logout | Não |
| `/accounts/dashboard/` | dashboard | Dashboard | ✅ Sim |
| `/accounts/profile/` | profile | Visualizar perfil | ✅ Sim |
| `/accounts/profile/edit/` | edit_profile | Editar perfil | ✅ Sim |
| `/accounts/password-change/` | password_change | Alterar senha | ✅ Sim |
| `/accounts/password_reset/` | password_reset | Recuperar senha | Não |
| `/accounts/reset/<token>/` | password_reset_confirm | Confirmar nova senha | Não |
| `/admin/` | admin | Painel administrativo | ✅ Sim |

---

## 📧 Configuração de Email

### Desenvolvimento (Console)
Por padrão, os emails aparecem no terminal:
```env
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### Produção (Gmail SMTP)
Configure o arquivo `.env`:
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_de_app
DEFAULT_FROM_EMAIL=seu_email@gmail.com
```

### Como gerar Senha de App do Gmail:
1. Acesse: https://myaccount.google.com/security
2. Ative "Verificação em duas etapas"
3. Vá em "Senhas de app"
4. Gere uma senha para "Email"
5. Use essa senha no `.env`

📖 **Documentação completa**: Veja `EMAIL_CONFIG.md`

---

## 📅 Diário de Modificações

### Versão 1.0.0 - Sistema Base (Inicial)
**Data**: Dezembro 2024

**Implementações:**
- ✅ Sistema de cadastro e login básico
- ✅ Dashboard protegido
- ✅ Página de perfil simples
- ✅ Logout funcional
- ✅ Templates base com HTML

**Arquivos criados:**
- `core/settings.py`, `core/urls.py`
- `accounts/views.py`, `accounts/urls.py`, `accounts/forms.py`
- `templates/base.html`, `templates/accounts/login.html`, `templates/accounts/register.html`

---

### Versão 1.1.0 - Estética e Design
**Data**: Dezembro 2024

**Melhorias:**
- ✅ Interface moderna com paleta roxa (#f4b1fd, #d190ff, #8e26e2)
- ✅ Botões animados com efeitos hover
- ✅ Fundo gradiente (azul escuro → roxo)
- ✅ Cards estilizados com efeito glass
- ✅ Mensagens de feedback visuais
- ✅ Ícones e emojis nas páginas

**Arquivos modificados:**
- `templates/base.html` - Adicionado CSS completo
- `templates/accounts/*.html` - Estilização de todas as páginas

---

### Versão 1.2.0 - Recuperação de Senha
**Data**: Dezembro 2024

**Implementações:**
- ✅ Sistema de recuperação de senha via email
- ✅ Token seguro com validade de 1 hora
- ✅ Templates personalizados de email
- ✅ Link "Esqueceu a senha?" na página de login
- ✅ Fluxo completo: solicitar → receber email → redefinir

**Arquivos criados:**
- `templates/accounts/password_reset.html`
- `templates/accounts/password_reset_done.html`
- `templates/accounts/password_reset_confirm.html`
- `templates/accounts/password_reset_complete.html`
- `templates/registration/password_reset_email.html`

**Arquivos modificados:**
- `accounts/urls.py` - Adicionadas rotas de recuperação
- `core/settings.py` - Configurações de email
- `templates/accounts/login.html` - Link de recuperação

---

### Versão 1.3.0 - Perfil com Avatar
**Data**: Dezembro 2024

**Implementações:**
- ✅ Modelo Profile com campo de avatar
- ✅ Upload de imagens (Pillow)
- ✅ Edição completa de perfil
- ✅ Exibição de avatar no perfil
- ✅ Alteração de senha para usuários logados
- ✅ Criação automática de perfil ao cadastrar

**Arquivos criados:**
- `accounts/models.py` - Modelo Profile
- `accounts/migrations/0001_initial.py` - Migration do Profile
- `templates/accounts/profile_edit.html`
- `templates/accounts/password_change.html`
- `templates/accounts/password_change_done.html`
- `create_profiles.py` - Script para criar perfis

**Arquivos modificados:**
- `accounts/forms.py` - Formulários de edição
- `accounts/views.py` - Views de edição e proteção
- `accounts/urls.py` - Rotas de edição
- `core/settings.py` - Configurações de mídia
- `core/urls.py` - Servir arquivos de mídia
- `templates/accounts/profile.html` - Exibição de avatar
- `requirements.txt` - Adicionado Pillow

---

### Versão 1.4.0 - Email Obrigatório e Segurança
**Data**: Dezembro 2024

**Implementações:**
- ✅ Campo email obrigatório no cadastro
- ✅ Variáveis de ambiente com python-dotenv
- ✅ Arquivo .env para credenciais
- ✅ Configuração Gmail SMTP funcional
- ✅ Senha de app do Gmail
- ✅ Documentação de configuração de email

**Arquivos criados:**
- `.env` - Variáveis de ambiente (não versionado)
- `.env.example` - Template de configuração
- `EMAIL_CONFIG.md` - Documentação de email

**Arquivos modificados:**
- `accounts/forms.py` - Email obrigatório
- `templates/accounts/register.html` - Campo de email
- `core/settings.py` - Carregamento de .env
- `.gitignore` - Adicionado .env e media/
- `requirements.txt` - Adicionado python-dotenv

---

### Versão 1.5.0 - Correções e Otimizações
**Data**: Dezembro 2024

**Correções:**
- ✅ Bug de navegação corrigido (perfil sem Profile)
- ✅ URLs de recuperação de senha padronizadas
- ✅ Proteção automática de criação de perfil
- ✅ Centralização e proporção de containers
- ✅ Instalação de python-dotenv no ambiente virtual

**Melhorias:**
- ✅ Script de teste de email
- ✅ Validação de configurações
- ✅ Mensagens de erro mais claras
- ✅ Documentação atualizada

---

## 📚 Melhorias Sugeridas

### Implementadas ✅
- [X] Recuperação de senha via email com token
- [X] Upload de foto de perfil
- [X] Edição completa de perfil
- [X] Alteração de senha
- [X] Email obrigatório no cadastro
- [X] Segurança com variáveis de ambiente
- [X] Interface moderna e responsiva

### Próximas Funcionalidades 🚀
- [ ] Verificação de email (confirmar email após cadastro)
- [ ] Login social (Google, Facebook, GitHub)
- [ ] Autenticação de dois fatores (2FA)
- [ ] Sistema de permissões e grupos
- [ ] API REST com Django REST Framework
- [ ] Testes automatizados (pytest)
- [ ] Paginação de usuários
- [ ] Histórico de login
- [ ] Tema claro/escuro
- [ ] Internacionalização (i18n)
- [ ] Deploy automatizado
- [ ] Logs de auditoria
- [ ] Rate limiting
- [ ] Captcha no cadastro

---

## 🐛 Troubleshooting

### Erro: "No module named django"
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Erro: "Table doesn't exist"
```bash
python manage.py migrate
```

### Erro: "No Profile for user"
```bash
python create_profiles.py
```

### Email não chega
1. Verifique o arquivo `.env`
2. Confirme a senha de app do Gmail
3. Verifique a pasta de SPAM
4. Veja os logs no terminal

### Erro: "Import dotenv could not be resolved"
```bash
pip install python-dotenv
```

---

## 🔒 Segurança

### Desenvolvimento
- DEBUG = True
- EMAIL_BACKEND = console
- SQLite3

### Produção
- [ ] DEBUG = False
- [ ] SECRET_KEY aleatória
- [ ] ALLOWED_HOSTS configurado
- [ ] HTTPS/TLS ativado
- [ ] PostgreSQL/MySQL
- [ ] EMAIL_BACKEND = SMTP
- [ ] Variáveis de ambiente no servidor
- [ ] Backup automático
- [ ] Monitoramento de logs

---

## 📁 Estrutura do Projeto

```
Sistema-login/
├── accounts/              # App de autenticação
│   ├── migrations/       # Migrações do banco
│   ├── forms.py          # Formulários
│   ├── models.py         # Modelo Profile
│   ├── urls.py           # Rotas
│   └── views.py          # Lógica
├── core/                 # Configurações
│   ├── settings.py       # Settings
│   └── urls.py           # URLs principais
├── templates/            # Templates HTML
│   ├── accounts/         # Templates de autenticação
│   └── registration/     # Templates de email
├── media/                # Uploads (avatars)
├── .env                  # Variáveis de ambiente
├── .env.example          # Template de .env
├── .gitignore            # Arquivos ignorados
├── create_profiles.py    # Script auxiliar
├── EMAIL_CONFIG.md       # Doc de email
├── manage.py             # Gerenciador Django
├── README.md             # Este arquivo
└── requirements.txt      # Dependências
```

---

## 📄 Licença

Este projeto é livre para uso educacional.

---

## 👨💻 Autor

**Kayque Brigadeiro**
- GitHub: [@Kayquebrigadeiro](https://github.com/Kayquebrigadeiro)
- Projeto: Sistema de Login Django

Desenvolvido como projeto de estudo de Django e boas práticas de desenvolvimento web.

---

## 📞 Suporte

Se encontrar problemas:

1. Verifique a seção [Troubleshooting](#troubleshooting)
2. Consulte o [Diário de Modificações](#diário-de-modificações)
3. Leia a [documentação oficial do Django](https://docs.djangoproject.com/)
4. Verifique se todas as dependências estão instaladas
5. Certifique-se de que o ambiente virtual está ativo

---

## 🎉 Pronto para Usar!

```bash
# Ative o ambiente virtual
venv\Scripts\activate

# Rode o servidor
python manage.py runserver

# Acesse
http://127.0.0.1:8000
```

**Sistema completo e funcional! 🚀**

---

## 📊 Estatísticas do Projeto

- **Linhas de código**: ~2.500+
- **Commits**: 15+
- **Funcionalidades**: 12+
- **Templates**: 10+
- **Tempo de desenvolvimento**: 1 dia
- **Versão atual**: 1.5.0

---

**Desenvolvido com ❤️ e Django**
