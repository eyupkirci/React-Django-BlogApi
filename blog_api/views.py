from django.http.response import HttpResponse
from .models import *
from .serializers import *
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>')
    
class ApiPostView(viewsets.ModelViewSet):

    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    class Meta:
        model= Post
        fields = '__all__'
