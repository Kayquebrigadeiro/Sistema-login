# 🚀 Deploy GRATUITO no PythonAnywhere

## Passo 1: Criar conta
1. Acesse: https://www.pythonanywhere.com/registration/register/beginner/
2. Crie conta gratuita (Beginner)

## Passo 2: Abrir Bash Console
1. Dashboard → "Consoles" → "Bash"

## Passo 3: Clonar projeto
```bash
git clone https://github.com/Kayquebrigadeiro/Sistema-login.git
cd Sistema-login
```

## Passo 4: Criar ambiente virtual
```bash
mkvirtualenv --python=/usr/bin/python3.10 myvenv
pip install -r requirements.txt
```

## Passo 5: Configurar banco de dados
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Passo 6: Configurar Web App
1. Dashboard → "Web" → "Add a new web app"
2. Escolha "Manual configuration"
3. Python 3.10

## Passo 7: Configurar WSGI
Clique no arquivo WSGI e cole:

```python
import os
import sys

path = '/home/SEUUSERNAME/Sistema-login'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Passo 8: Configurar Virtualenv
Na seção "Virtualenv":
```
/home/SEUUSERNAME/.virtualenvs/myvenv
```

## Passo 9: Configurar Static Files
Na seção "Static files":
- URL: `/static/`
- Directory: `/home/SEUUSERNAME/Sistema-login/staticfiles`

## Passo 10: Coletar arquivos estáticos
No Bash:
```bash
cd ~/Sistema-login
python manage.py collectstatic
```

## Passo 11: Atualizar ALLOWED_HOSTS
No arquivo `core/settings.py`, adicione:
```python
ALLOWED_HOSTS = ['seuusername.pythonanywhere.com']
```

## Passo 12: Reload
Clique em "Reload" no topo da página Web

## ✅ Pronto!
Acesse: https://seuusername.pythonanywhere.com
