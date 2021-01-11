from django.urls import path
from . import views


urlpatterns = [
    path('rec/', views.performed_train_rec),
    path('<str:train_type>/', views.train),
]
