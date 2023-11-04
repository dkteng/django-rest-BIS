from django.urls import path, re_path
from . import views

urlpatterns = [
    path('books/', views.getBooks),
    path('books/<int:pk>/', views.getBook),
    path('books/create/', views.createBook),
    path('books/update/<int:pk>/', views.updateBook),
    path('books/delete/<int:pk>/', views.deleteBook),
    path('books/available/', views.AvailableBooks.as_view()),
    path('books/borrowed/', views.borrowedBooks),

    path('users/', views.getUsers),
    path('users/<int:pk>/', views.getUser),

    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test-token',views.test_token),
]