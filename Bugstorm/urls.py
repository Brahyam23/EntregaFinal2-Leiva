"""Bugstorm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from index.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('not_found/', not_found, name="not_found"),
    path('routes/', routes, name="routes"),
    path('about/', about, name="about"),
    path('', index, name='index'),
    path('notice/', include('index.urls')),
    path('accounts/', include('user.urls')),
    path('gallery/', include('gallery.urls')),
    path('forum/', include('forum.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "index.views.handle_not_found"
