from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated


from .models import (User, Book, BookUser)
from .serializers import (BookSerializer, BookUserSerializer)


class BookListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookUserListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookUserSerializer
    queryset = Book.objects.all()

class BookUserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookUserSerializer
    queryset = BookUser.objects.all()

class MyBookListing(ListAPIView):
    serializer_class = BookUserSerializer

    def get_queryset(self):
        return BookUser.objects.filter(user = self.request.user)