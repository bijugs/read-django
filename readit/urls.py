"""readit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    re_path(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name='author-detail')
"""
from django.contrib import admin
from django.urls import path,re_path

from books.views import (AuthorDetail, AuthorList, BookDetail, list_books, CreateAuthor,
                        CreateBook, ReviewList, review_book)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_books, name='books'),
    path('authors/', AuthorList.as_view(), name='authors'),
    re_path(r'^books/add/$', CreateBook.as_view(), name='add-book'),
    re_path(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
    re_path(r'^authors/add/$', CreateAuthor.as_view(), name='add-author'),
    re_path(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name='author-detail'),
    re_path(r'^review/$', ReviewList.as_view(), name='review-books'),
    re_path(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
]
