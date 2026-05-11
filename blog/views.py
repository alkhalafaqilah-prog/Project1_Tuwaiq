from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Category, Comment, Post
from django.shortcuts import get_object_or_404

# Create your views here.
def main_view(request):
    return render(request, 'blog/main.html')

def users_view(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {'users': users})

def blogs_view(request):
    # This retrieves all blog posts from the database
    all_blogs = Post.objects.all()
    # Sends the posts to the template
    return render(request, 'blog/blogs.html', {'blogs': all_blogs})


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})

def comments_view(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments})

def blog_detail(request, id):
    # This finds a specific blog by its ID or returns a 404 error if not found
    blog = get_object_or_404(Post, id=id)
    return render(request, 'blog/blogdetails.html', {'blog': blog})