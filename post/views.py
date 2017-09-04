from django.shortcuts import render
from .models import Post, Category


def about_me(request):
    return render(request, 'post/about_me.html')


def articles(request):
    return render(request, 'post/articles.html', {
        'posts': Post.objects.all()[:5],
        'categories': Category.objects.all()[:10],
    })


def article(request, id):
    return render(request, 'post/article.html', {
        'post': Post.objects.get(id=id)
    })
