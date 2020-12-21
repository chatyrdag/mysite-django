from django.urls import path
from .views import CategoryListView, PostDetailView


urlpatterns = [
    path('', CategoryListView.as_view(), name='posts-category-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='posts-post-detail'),
]
