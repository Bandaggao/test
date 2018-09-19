from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


urlpatterns = [
     #url(r'^admin/', admin.site.urls),
     #url(r'^music/', include('music.urls')),

    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
]
