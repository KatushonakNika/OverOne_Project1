from django.shortcuts import render
from .models import Article

def blog(request):
    blog = Article.objects.order_by('title')
    return render(request, 'blog/blog.html', {'blog': blog})

