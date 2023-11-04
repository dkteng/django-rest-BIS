from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer, UserSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status


# custom pagination class
class Pagination(LimitOffsetPagination):
    default_limit = 10

#get all books
@api_view(['GET'])
def getBooks(request):
    paginator = Pagination()
    books = Book.objects.all()
    paginated = paginator.paginate_queryset(books, request)
    serializer = BookSerializer(paginated, many=True)
    return paginator.get_paginated_response(serializer.data)

#get single book
@api_view(['GET'])
def getBook(request, pk):
    book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
    
#create book (admin only)
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def createBook(request):
    if request.method == 'POST':
        data = request.data
        serializer = BookSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update book (admin only)
@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def updateBook(request, pk):
    if request.method == 'PATCH':
        book = get_object_or_404(Book, id=pk)
        data = request.data
        serializer = BookSerializer(book, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete book (admin only)
@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def deleteBook(request, pk):
    if request.method == 'DELETE':
        book = get_object_or_404(Book, id=pk)
        book.delete()
        return Response(f'{request.user.username} deleted book {book.title}', status=status.HTTP_204_NO_CONTENT)
    
#get available books + count
class AvailableBooks(APIView):
    def get(self, request):
        books = Book.objects.all()
        count = 0
        available = []
        for book in books:
            if not book.borrowed:
                count += 1
                available.append(book)
        serializer = BookSerializer(instance=available, many=True)
        return Response({'available book count': count, 'books': serializer.data}, status=status.HTTP_200_OK)
    
#get borrowed books + borrower + count (user + admin only)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def borrowedBooks(request):
    count = 0
    fields = ['title', 'author', 'genre', 'borrowed', 'borrowed_by', 'borrow_date', 'due_date']
    books = Book.objects.all().values(*fields)
    borrowed = []
    for book in books:
        if book.get('borrowed'):
            count += 1
            user = User.objects.get(id=book['borrowed_by'])
            book['user'] = {'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name}
            borrowed.append(book)    
    return Response({'count': count, 'books': borrowed}, status=status.HTTP_200_OK)






# create/signup user
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#login user
@api_view(['POST'])
def login(request):
    try:
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"detail" : "Not found."}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance= user, many=False)
        return Response({'token': token.key, 'user': serializer.data})
    except KeyError:
        return Response({"error": "'username' & 'password' required"},status=status.HTTP_400_BAD_REQUEST)

#test user token
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response(f"{request.user.username} passed!")






#get all users + count (admin only)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def getUsers(request):
    paginator = Pagination()
    users = User.objects.all()
    paginated = paginator.paginate_queryset(users, request)
    serializer = UserSerializer(paginated, many=True)
    return paginator.get_paginated_response(serializer.data)

#get single user (admin only)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def getUser(request, pk):
    user = get_object_or_404(User,id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)