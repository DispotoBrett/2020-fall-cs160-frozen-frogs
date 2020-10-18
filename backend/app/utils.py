import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

def upload_img(django_img, path):
    content = ContentFile(django_img.read())
    default_storage.save(path, content)
    print(os.path.join(settings.MEDIA_ROOT, path))
