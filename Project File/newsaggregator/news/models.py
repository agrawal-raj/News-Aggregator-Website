from django.db import models # type: ignore

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateTimeField()
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=+True)
    
    
    def __str__(self):
        return self.title