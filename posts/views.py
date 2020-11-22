from django.shortcuts import render
from .models import Tag, Category, Post


def category(request, category):
    category_query = Category.objects.filter(slug=category)
    category_id = category_query[0].id
    category = category_query[0]
    posts = Post.objects.filter(category_post=category_id).order_by('id')
    return render(request, 'category.html', {
        'posts': posts,
        'category': category
    })


def post(request, category, post):
    category_query = Category.objects.filter(slug=category)
    category_qs = category_query[0]
    post_query = Post.objects.filter(slug=post)
    tags = post_query[0].tags.all()
    return render(request, 'post.html', {
        'post': post_query[0],
        'category': category_qs,
        'tags': tags
    })


def tag(request, tag):
    tag_query = Tag.objects.filter(slug=tag)
    tag_name = tag_query[0].tag_name
    posts = tag_query[0].post_set.all()
    return render(request, 'tag.html', {
        'posts': posts,
        'tag_name': tag_name
    })
