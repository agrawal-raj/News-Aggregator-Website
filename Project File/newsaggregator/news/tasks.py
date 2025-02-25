from celery import shared_task
from news.fetch_news import fetch_news

@shared_task
def fetch_news_task():
    categories= ['business', 'entertainment', 'general', 'health', 'science', 'sports','technology']
    for category in categories:
        fetch_news(category=category)
    return "News data fetched successfully!"
