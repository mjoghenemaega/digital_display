# views.py
from django.shortcuts import render
from .models import News
from django.http import Http404

def news_view(request):
    context = {
        'featured_news': News.objects.filter(category='featured')[:3],
        'popular_news': News.objects.filter(category='popular')[:4],
        'latest_news': News.objects.filter(category='latest')[:3],
        'most_viewed_news': News.objects.filter(filter='most_viewed')[:3],
        'most_read_news': News.objects.filter(filter='most_read')[:3],
        'most_recent_news': News.objects.filter(filter='most_recent')[:3],
        'technology': News.objects.filter(category='technology')[:3],
        'sports': News.objects.filter(category='sports')[:3],
        'nieee': News.objects.filter(category='nieee')[:3],
        'college': News.objects.filter(category='college')[:3],
    }
    return render(request, 'news.html', context)


def news_detail(request, news_id):
    try:
        news_item = News.objects.get(id=news_id)
    except News.DoesNotExist:
        raise Http404("News item not found")
    return render(request, 'news_detail.html', {'news_item': news_item, 'popular_news': News.objects.filter(category='popular')[:4],})