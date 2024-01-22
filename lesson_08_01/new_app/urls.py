import imp
from .views import post_detail
from .views import category_list
from .views import category_detail
from django.urls import path

urlpatterns = [
    path('<int:pk>/', post_detail, name='post_detail'),
    path('', category_list, name='category_list'),
    path('<int:pk>/', category_detail, name='category_detail')
]

