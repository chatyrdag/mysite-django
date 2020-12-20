from django.core import paginator
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from .models import PostBlog, TagBlog, CategoryBlog


class PostBlogListView(ListView):
    model = PostBlog
    paginate_by = 5


class PostBlogDetailView(DetailView):
    model = PostBlog

    def get_context_data(self, **kwargs):
        post = self.get_object()
        context = super().get_context_data(**kwargs)
        post.hits += 1
        post.save()
        return context

class TagBlogDetailView(DetailView):
    model = TagBlog
    post_paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TagBlogDetailView, self).get_context_data(**kwargs)
        posts = PostBlog.objects.filter(tags=context['tagblog'].id).order_by('-created_at')
        post_paginator = paginator.Paginator(posts, self.post_paginate_by)
        page = self.request.GET.get('page')
        try:
            page_obj = post_paginator.page(page)
        except (paginator.PageNotAnInteger, paginator.EmptyPage):
            page_obj = post_paginator.page(1)
        context['page_obj'] = page_obj
        if post_paginator.count > self.post_paginate_by:
            context['is_paginated'] = True
        return context


class CategoryBlogDetailView(DetailView):
    model = CategoryBlog
    post_paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CategoryBlogDetailView, self).get_context_data(**kwargs)
        posts = PostBlog.objects.filter(category=context['categoryblog'].id).order_by('-created_at')
        post_paginator = paginator.Paginator(posts, self.post_paginate_by)
        page = self.request.GET.get('page')
        try:
            page_obj = post_paginator.page(page)
        except (paginator.PageNotAnInteger, paginator.EmptyPage):
            page_obj = post_paginator.page(1)
        context['page_obj'] = page_obj
        if post_paginator.count > self.post_paginate_by:
            context['is_paginated'] = True
        return context
