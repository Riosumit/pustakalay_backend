from django.contrib import admin
from django.urls import path, include
from .views import LibrarianLoginView

urlpatterns = [
    path('login', LibrarianLoginView.as_view(), name='librarian_login'),
]