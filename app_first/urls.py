from django.urls import path, include
from allauth.account.views import login, logout
from app_first import views
from app_first.views import AuthorEdit, AuthorList

app_name = 'app_first'
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publisher_list),
    path('author/create/', AuthorEdit.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('friends/', views.friends_list),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]