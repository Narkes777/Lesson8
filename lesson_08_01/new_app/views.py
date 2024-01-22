from unicodedata import category
from django.shortcuts import render
from .models import Post, Category
from django.http import HttpResponse, HttpRequest

from django.shortcuts import get_object_or_404

# Create your vies here

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    return HttpResponse(post)
    # try:
    #     post = Post.objects.get(pk=pk)
    #     return HttpResponse(post.author_id.name)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound(f'Объект с ключем {pk} не был найден')

def category_list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return HttpResponse(categories)

def category_detail(request: HttpRequest, pk: int) -> HttpResponse:
    category = Category.objects.get(pk=pk)
    #1 
    posts = Post.objects.filter(categories=category)
    #2
    posts = category.post_set.all()
    result = ''
    for post in posts:
        result += str(post)
    result += category.name
    return HttpResponse(result)