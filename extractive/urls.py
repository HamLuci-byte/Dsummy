from django.urls import path
from . import views

app_name = 'extractive'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('webscraping/', views.scrap, name= 'webscrap'),
    path('compare/', views.compare, name= 'compare'),
    #path('blog/', views.blog, name= 'blog'),
    path('blog/<int:my_id>/', views.bloglookup, name= 'bloglook'),
]