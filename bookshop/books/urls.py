from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('',views.index,name="index"),
    path('bookstore2/',views.bookstore2,name="bookstore2"),
    path('bookstore3/',views.bookstore3,name="bookstore3"),
    path('addbook/',views.addbook,name="addbook"),
    path('search/',views.search,name="search")
    
    
]