# views.py
from django.shortcuts import render
from .models import News

def news_view(request):
    context = {
        'featured_news': News.objects.filter(category='featured')[:3],
        'popular_news': News.objects.filter(category='popular')[:3],
        'latest_news': News.objects.filter(category='latest')[:3],
        'most_viewed_news': News.objects.filter(category='most_viewed')[:3],
        'most_read_news': News.objects.filter(category='most_read')[:3],
        'most_recent_news': News.objects.filter(category='most_recent')[:3],
    }
    return render(request, 'news.html', context)
