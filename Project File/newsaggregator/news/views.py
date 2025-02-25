from django.shortcuts import render
from news.models import Article
from google.cloud import translate_v2 as translate


# Create your views here.
import requests

def translate_text(text, target_lang):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_lang)
    return result['translateText']


def home(request):
    category= request.GET.get('category', '')
    source= request.GET.get('source', '')
    
    articles= Article.objects.all().order_by('published_at')
    
    # Apply filters
    if category:
        articles = articles.filter(category__iexact=category)
    if source:
        articles = articles.filter(source__iexact=source)
    
    # get a unique categories and sources for dropdowns
    categories= Article.objects.values_list('category', flat=True).distinct()
    sources= Article.objects.values_list('source', flat=True).distinct()
    
    
    return render(request, 'news/home.html',{
        'articles': articles,
        'categories': categories,
        'sources': sources,
    })
    
    articles = Article.objects.all()
    target_lang = request.Get.get('lang', 'en')
    
    translated_articles = []
    for article in articles:
        translated_articles.append({
            'title': translate_text(article.title, target_lang),
            'description': translate_text(article.description, target_lang),
            'url': article.url,
            'source': article.source,
            'published_at': article.published_at,
            'category': translate_text(article.category,target_lang),
        })
        
    return render(request, 'news/home.html', {
        'articles': translate_articles,
        'categories': Article.objects.values_list('category', flat=True).distinct(),
        'sources': Article.objects.values_list('source', flat=True).distinct(),
    })
    
url = "https://newsapi.org/v2/everything?q=apple&from=2025-02-07&to=2025-02-07&sortBy=popularity&apiKey=be4ca9a66fc4426a997c4f343cbb282a"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

