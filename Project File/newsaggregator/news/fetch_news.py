import requests
from django.utils import timezone
from news.models import Article


def fetch_news():
    api_key= "be4ca9a66fc4426a997c4f343cbb282a"
    url= f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    data= response.json()
    
    for item in data['articles']:
        Article.objects.create(
            title= item['title'],
            description = item['description'],
            url = item['url'],
            published_at = timezone.now(),
            source = item['source']['name']
            
        )
        
if __name__== '__main__':
    fetch_news()