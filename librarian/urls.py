from django.contrib import admin
from django.urls import path, include
from .views import LibrarianLoginView, StudentResistrationView

urlpatterns = [
    path('login', LibrarianLoginView.as_view(), name='librarian_login'),
    path('register/student', StudentResistrationView.as_view(), name='student_registeration')
]