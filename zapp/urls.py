from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.loading, name='loading'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('index.html', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('index-2.html', views.index_2, name='index_2'),

    path('movie.html', views.movie, name='movie'),
    path('movie-details.html', views.movie_details, name='movie_details'),
    path('tv-show.html', views.tv_show, name='tv_show'),
    path('pricing.html', views.pricing, name='pricing'),
    path('blog.html', views.blog, name='blog'),
    path('blog-details.html', views.blog_details, name='blog_details'),
    path('contact.html', views.contact, name='contact')

]