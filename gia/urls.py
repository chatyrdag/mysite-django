from django.urls import path
from .views import GIAList, ShowSolution


urlpatterns = [
    path('show/<slug:slug>/', ShowSolution.as_view()),
    path('<str:exam>/', GIAList.as_view()),
    path('<str:exam>/<int:task>/', GIAList.as_view())
]
