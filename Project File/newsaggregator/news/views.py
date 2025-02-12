from django.shortcuts import render
from news.models import Article

# Create your views here.
import requests

def home(request):
    articles= Article.objects.all().order_by('published_at')
    return render(request, 'news/home.html', {'articles':articles})

url = "https://newsapi.org/v2/everything?q=apple&from=2025-02-07&to=2025-02-07&sortBy=popularity&apiKey=be4ca9a66fc4426a997c4f343cbb282a"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

