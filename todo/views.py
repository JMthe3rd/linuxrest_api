
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.core import serializers
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] #permissions.IsAuthenticated

    def create(self, request):
        todo = Todo.objects.create(title=request.data.get('title'),
                                   description=request.data.get('description'),
                                   user=request.user,
                                   )
        serialized_obj = serializers.serialize('json', [todo,])
        return HttpResponse(serialized_obj, content_type='applocation/json')