from django.urls import path, re_path
from . import views

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Book Inventory System API",
      default_version='v1',
      description="book inventory system api using rest framework in django",
      terms_of_service="",
      contact=openapi.Contact(email="contact@BIS.api.local"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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

    path('ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]