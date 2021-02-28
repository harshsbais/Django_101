from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    # If you want to allow GET for everyone and all ops for authenticated users
    permission_classes = [IsAuthenticatedOrReadOnly]
