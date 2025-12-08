import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile

# Criar perfis para usuários que não têm
for user in User.objects.all():
    Profile.objects.get_or_create(user=user)
    print(f'Profile criado/verificado para {user.username}')

print('Concluído!')
