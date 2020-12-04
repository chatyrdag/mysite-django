from django.shortcuts import render
from .models import Tag, Category, Post


def category(request, category):
    category_query = Category.objects.filter(slug=category)
    category_qs = []
    posts = []
    if category_query:
        category_id = category_query[0].id
        category_qs = category_query[0]
        posts = Post.objects.filter(category_post=category_id).order_by('id')
    return render(request, 'category.html', {
        'posts': posts,
        'category': category_qs
    })


def post(request, category, post):
    tags_qs = ''
    post_qs = []
    category_qs = []

    category_query = Category.objects.filter(slug=category)
    if category_query:
        category_qs = category_query[0]

    post_query = Post.objects.filter(slug=post)
    if post_query:
        tags_qs = post_query[0].tags.all()
        post_qs = post_query[0]

    return render(request, 'post.html', {
        'post': post_qs,
        'category': category_qs,
        'tags': tags_qs
    })


def tag(request, tag):
    tag_name = ''
    posts = []
    tag_query = Tag.objects.filter(slug=tag)

    if tag_query:
        tag_name = tag_query[0].tag_name
        posts = tag_query[0].post_set.all()

    return render(request, 'tag.html', {
        'posts': posts,
        'tag_name': tag_name
    })
