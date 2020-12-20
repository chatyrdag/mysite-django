from django.urls import path
from .views import PostBlogListView, PostBlogDetailView, TagBlogDetailView, CategoryBlogDetailView


urlpatterns = [
    path('tag/<slug:slug>/', TagBlogDetailView.as_view(), name='tagblog-detail'),
    path('category/<slug:slug>/', CategoryBlogDetailView.as_view(), name='categoryblog-detail'),
    path('<slug:slug>/', PostBlogDetailView.as_view(), name='postblog-detail'),
    path('', PostBlogListView.as_view(), name='blog-list'),
]
