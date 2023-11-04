from rest_framework.serializers import ModelSerializer
from .models import Book, User

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta: 
        model = User
        fields = ['id','email','username','first_name','last_name']