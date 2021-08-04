from django.shortcuts import render, get_object_or_404
from .models import Category, Article
from django.conf import settings


def index(request):
    all_categories = Category.objects.all()
    all_articles = reversed(Article.objects.all())
    latest_articles = Article.objects.all().order_by('-Date')[:3]
    context = {
        'all_categories': all_categories,
        'all_articles': all_articles,
        'latest_articles': latest_articles
    }
    return render(request, 'index.html', context)

def detail(request, article_id):
    articles = get_object_or_404(Article, pk=article_id)

    context = {
        'articles': articles
    }
    return render(request, 'pages/index-inner.html', context)
    

def category(request, category_id):
    categories = get_object_or_404(Category, pk=category_id)
    all_categories = Category.objects.all()

    context = {
        'categories': categories,
        'all_categories': all_categories
    }
    return render(request, 'pages/category.html', context)


def about(request):
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories,
    }
    return render(request, 'pages/aboutus.html', context)


def contact(request):
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories,
    }
    return render(request, 'pages/contactus.html', context)
