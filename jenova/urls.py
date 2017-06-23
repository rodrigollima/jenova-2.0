from django.conf.urls import url
from django.contrib import admin
from jenova.core import views as core

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', core.dashboard),
    url(r'^login', core.login, name='login'),
]
