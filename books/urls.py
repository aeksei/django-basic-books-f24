"""
URL configuration for django_basic_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""
from django.urls import path

from books import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("about_library/", views.about, name="about"),
    path("current_datetime/", views.get_current_datetime),
    path("books/", views.get_books, name="book-list"),
    path("books/random/", views.get_random_book),
    path("books/<int:book_id>/", views.get_book, name="book-detail"),
]
