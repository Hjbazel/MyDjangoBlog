from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    #thumbnail
    #author
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+'...'
