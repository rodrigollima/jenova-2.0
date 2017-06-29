from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from jenova.core import views as core

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core.dashboard),

    #url(r'^login', core.login, name='login'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
