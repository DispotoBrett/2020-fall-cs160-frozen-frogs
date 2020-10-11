from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

# url paths
urlpatterns = [ 
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('createPosting', views.create_posting, name='create'),
    path('savePosting', views.save_posting, name='save'),
    path('posting/<int:posting_id>', views.get_posting, name='get'),
    path('browse', views.browse, name='browse'),
    path('list_book', views.list_book, name='list_book'),
    path('view_book/<book_id>', views.view_book, name='view_book'),
    path('login', auth_views.LoginView.as_view()),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout')


] + static(settings.STATIC_URL)

APPEND_SLASH = True