from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('users/', views.users_view, name='users'),
    path('blogs/', views.blogs_view, name='blogs'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    # Add paths for categories and comments similarly...
]