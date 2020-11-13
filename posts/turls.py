from django.urls import path
from . import views


urlpatterns = [
    path('<slug:tag>/', views.tag)
]
