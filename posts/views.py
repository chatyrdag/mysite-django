from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Tag, Category, Post


class CategoryListView(ListView):
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Post.objects.filter(category_post=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class PostDetailView(DetailView):
    model = Post


class TagDetailView(DetailView):
    model = Tag
