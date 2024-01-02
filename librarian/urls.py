from django.contrib import admin
from django.urls import path, include
from .views import LibrarianLoginView, StudentView, BookView

urlpatterns = [
    path('login', LibrarianLoginView.as_view(), name='librarian_login'),
    path('students', StudentView.as_view(), name='student_list'),
    path('student/<int:pk>', StudentView.as_view(), name='student_details'),
    path('books', BookView.as_view(), name='book_list'),
    path('book/<int:pk>', BookView.as_view(), name='book_details')
]