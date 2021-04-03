from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    # permission_classes = [permissions.AllowAny, ]
    queryset = Todo.objects.all()