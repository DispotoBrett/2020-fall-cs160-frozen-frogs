import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from app.models import Favorite

def upload_img(django_img, path):
    content = ContentFile(django_img.read())
    default_storage.save(path, content)
    print(os.path.join(settings.MEDIA_ROOT, path))

def get_favorites(user):
    favorites = []
    for record in Favorite.objects.filter(user=user):
        favorites.append(record.posting_id)

    return favorites