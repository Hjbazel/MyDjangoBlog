from django.shortcuts import render
from . import models

# Create your views here.
def articles_list(request):
    articles=models.Articles.objects.all().order_by('date')
    arg={'articles':articles}
    return render(request, 'articles/articleslist.html',arg)
