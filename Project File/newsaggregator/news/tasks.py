from celery import shared_task
from news.fetch_news import fetch_news

@shared_task
def fetch_news_task():
    fetch_news()
    return "News data fetched successfully!"
