from rest_framework import serializers
from .models import *
from django.db.models import fields
from django.db import models



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'
    
    