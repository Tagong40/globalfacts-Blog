from django.contrib import admin
from .models import Category, Post, Tag, Author, commet

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(commet)