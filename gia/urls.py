from django.urls import path
from . import views


urlpatterns = [
    path('show/<slug:task>/', views.show),
    path('<str:exam>/', views.gia),
    path('<str:exam>/<int:task>/', views.gia),
    path('<str:exam>/<int:task>/<int:offset>/', views.gia)
]
