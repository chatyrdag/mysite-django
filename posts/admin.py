from django.contrib import admin
from .models import Tag, Post, Category


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
