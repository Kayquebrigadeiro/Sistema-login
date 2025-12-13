# 📧 Configuração de Email

## 🔐 Segurança com Variáveis de Ambiente

As credenciais de email estão protegidas usando variáveis de ambiente.

## 📝 Como configurar:

### 1. Copie o arquivo de exemplo:
```bash
cp .env.example .env
```

### 2. Edite o arquivo `.env` com suas credenciais:
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_de_app
DEFAULT_FROM_EMAIL=seu_email@gmail.com
```

## 🔑 Gmail - Senha de App:

1. Acesse: https://myaccount.google.com/security
2. Ative "Verificação em duas etapas"
3. Vá em "Senhas de app"
4. Gere uma senha para "Email"
5. Use essa senha no `.env`

## 📮 Hotmail/Outlook:

```env
EMAIL_HOST=smtp-mail.outlook.com
EMAIL_HOST_USER=seu_email@hotmail.com
```

## 🧪 Modo de Desenvolvimento (Console):

Para testar sem enviar emails reais:
```env
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

## ⚠️ IMPORTANTE:

- **NUNCA** faça commit do arquivo `.env`
- O `.env` está no `.gitignore`
- Use `.env.example` como template
- Em produção, use variáveis de ambiente do servidor

## 🚀 Testando:

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/accounts/password_reset/
