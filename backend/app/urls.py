from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

# url paths
urlpatterns = [ 
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('createPosting', views.create_posting, name='create'),
    path('savePosting', views.save_posting, name='save'),
    path('posting/<int:posting_id>', views.get_posting, name='get'),
    path('browse', views.browse, name='browse')
] + static(settings.STATIC_URL)
