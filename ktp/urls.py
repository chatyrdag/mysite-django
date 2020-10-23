from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:form>/<int:discipline>/', views.ktp),
]
