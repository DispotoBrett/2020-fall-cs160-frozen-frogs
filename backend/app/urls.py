from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

# url paths
urlpatterns = [ 
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('posting', views.my_postings, name='my_postings'),
    path('posting/<posting_id>', views.get_posting, name='posting'),
    path('browse', views.browse, name='browse'),
    path('list_book', views.list_book, name='list_book'),
    path('login', views.login_view, name='login' ),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('favorite/<posting_id>', views.favorite, name='favorite'),
    path('report/<posting_id>', views.report, name='report'),
    path('chat', views.chat, name='chat'),
    path('chat/<other_user_id>', views.chat, name='chat'),
    path('chat/<other_user_id>/<posting_id>', views.chat, name='chat'),
    path('message/<other_user_id>', views.message, name='message'),
] + static(settings.STATIC_URL)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

APPEND_SLASH = True
