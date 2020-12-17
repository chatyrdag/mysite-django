from django.contrib import admin
from .models import CategoryBlog, TagBlog, PostBlog


admin.site.register(CategoryBlog)
admin.site.register(TagBlog)
admin.site.register(PostBlog)
