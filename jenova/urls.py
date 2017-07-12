from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from jenova.core import views as core
from jenova.client.views import ClientView
from jenova.domain import views as domain_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core.dashboard),
<<<<<<< HEAD
    
=======
    url(r'^area51', core.dashboard2),
    #url(r'^login', core.login, name='login'),
>>>>>>> 0dd51997b95f05a1b4374050d498850903221df3
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^domain/', domain_views.list, name='domain_list'),

    url(r'^client/', ClientView.as_view()),
]
