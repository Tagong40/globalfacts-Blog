
from django.urls import path, include
from .views import index, category, indexDetail

urlpatterns = [
    path('', index, name="index"),
    path('post-category/<slug>/', category, name="category"),
    path('post-by/<slug>/', indexDetail, name="detail"),
]
