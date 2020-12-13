from django.urls import path
from .views import CategoryListView, PostDetailView


urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<slug:slug>/', PostDetailView.as_view()),
]
