from django.shortcuts import render

from .models import Article, Comment

def index(request):
    lates_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'lates_articles_list': lates_articles_list})