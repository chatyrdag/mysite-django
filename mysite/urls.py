"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import UserLoginForm


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ktp/', include('ktp.urls')),
    path('gia/', include('gia.urls')),
    path('mathapi/', include('mathapi.urls')),
    path('admin/', admin.site.urls),
    path('tag/', include('posts.turls')),
    path('blog/', include('blog.urls')),
    path('train/', include('train.urls')),
    path('<slug:category>/', include('posts.urls')),
    path('', views.main),
]
