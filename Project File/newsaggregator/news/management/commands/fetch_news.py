from django.core.management.base import BaseCommand
from news.fetch_news import fetch_news


class Command(BaseCommand):
    help= 'Fetches the latest news from NewsAPI'
    
    def handle(self, *args, **kwargs):
        fetch_news()
        self.stdout.write(self.style.SUCCESS('Success fetched news articles'))
        # return super().handle(*args, **options)