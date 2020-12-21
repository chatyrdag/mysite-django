from django.urls import path
from .views import TagDetailView

urlpatterns = [
    path('<slug:slug>/', TagDetailView.as_view(), name='posts-tag-detail'),
]
