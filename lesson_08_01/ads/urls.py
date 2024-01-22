from django.urls import path
from .views import index, ad_list, AdCreateView, search_by_name

urlpatterns = [
    path('<int:pk>/', index, name='ad_detail'), # /1 /2 /101241
    path('create/', AdCreateView.as_view(), name='create_ad'),
    path('', ad_list),
    path('<str:name>', search_by_name)
]

