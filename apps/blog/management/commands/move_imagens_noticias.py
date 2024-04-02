import os
from shutil import copy
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Carrega a fixture e move os arquivos de imagem para o local correto'

    def handle(self, *args, **kwargs):
        # Carrega a fixture
        os.system('python manage.py loaddata noticia.json')

        # Move os arquivos de imagem
        image_static_dir = os.path.join(settings.BASE_DIR, 'core/static/img/noticias')
        image_dir = os.path.join(settings.MEDIA_ROOT, 'core/static/img/noticias')

        # Verifica se o diretório image_dir existe, se não, cria
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        for filename in os.listdir(image_static_dir):
            if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
                src = os.path.join(image_static_dir, filename)
                dst = os.path.join(image_dir, filename)
                copy(src, dst)

        self.stdout.write(self.style.SUCCESS('Fixture carregada com sucesso e imagens movidas.'))
