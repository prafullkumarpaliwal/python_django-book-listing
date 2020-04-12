from rest_framework import serializers

from .models import (User, Book, BookUser)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookUser
        fields = '__all__'