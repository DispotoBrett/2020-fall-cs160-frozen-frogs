from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

# url paths
urlpatterns = [ 
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile')
] + static(settings.STATIC_URL)
