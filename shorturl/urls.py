"""shorturl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from short.views import get_name, get_url, get_list, get_del, get_sign, get_login, logout
from short.models import User

urlpatterns = [
    path('', get_name),
    path('signup', get_sign),
    path('login', get_login),
    path('logout', logout),
    path('list', get_list),
    path('<str:name>', get_url),
    path('admin/', admin.site.urls),
    path('delete/id=<str:id>', get_del),

]
