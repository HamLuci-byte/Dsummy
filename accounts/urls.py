from django.urls import path
from . import views

#from pages.views import home_view, contact_view, about_view
# another way

app_name = 'accounts'
urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),  
    #path('about.html/', views.about, name='about'), 
]