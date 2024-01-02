from django.contrib import admin
from django.urls import path, include
from .views import LibrarianLoginView, StudentResistrationView, BookView

urlpatterns = [
    path('login', LibrarianLoginView.as_view(), name='librarian_login'),
    path('register/student', StudentResistrationView.as_view(), name='student_registeration'),
    path('books', BookView.as_view(), name='book_list'),
    path('book/<int:pk>', BookView.as_view(), name='book_details')
]